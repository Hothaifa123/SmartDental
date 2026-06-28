from flask import Flask, request, jsonify, render_template, redirect, Response, send_from_directory
from flask_cors import CORS
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import json, os, urllib.parse
from database import init_db, get_db
from models import User, Patient, Drug, Prescription, EmergencyProtocol
from config import UPLOAD_FOLDER, DEVELOPER_INFO, GEMINI_API_KEY
from utils.prescription_engine import generate_pdf_bytes
from utils.smart_checker import check_interactions, auto_adjust_dose

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
init_db()

db = get_db()
if db.query(User).filter_by(username='Hothaifa123').first() is None:
    db.add(User(username='Hothaifa123', password_hash=generate_password_hash('hothaifa112233'), is_admin=True, is_active=True, doctor_name=DEVELOPER_INFO['name'], doctor_phone=DEVELOPER_INFO['phone'], clinic_name=DEVELOPER_INFO['clinic']))
if db.query(Drug).count() == 0:
    from data.drug_database import ALL_DRUGS
    for d in ALL_DRUGS: db.add(Drug(**d))
if db.query(EmergencyProtocol).count() == 0:
    from data.emergency_protocols import EMERGENCIES
    for e in EMERGENCIES: db.add(EmergencyProtocol(**e))
db.commit()
db.close()

@login_manager.user_loader
def load_user(uid):
    return get_db().query(User).get(int(uid))

@app.context_processor
def inject_user():
    return dict(current_user=current_user)

@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        user = db.query(User).filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            if not user.is_active: return render_template('login.html', error='Account disabled.')
            login_user(user, remember=True)
            return redirect('/')
        return render_template('login.html', error='Invalid credentials.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        if len(username) < 3 or len(password) < 6:
            return render_template('register.html', error='Username 3+ chars, password 6+ chars')
        db = get_db()
        if db.query(User).filter_by(username=username).first():
            return render_template('register.html', error='Username already exists')
        db.add(User(username=username, password_hash=generate_password_hash(password), is_active=True))
        db.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# API Drugs
@app.route('/api/drugs')
@login_required
def drugs():
    db = get_db()
    return jsonify([{'id':d.id,'trade_name':d.trade_name,'category':d.category,'admin_route':d.admin_route,'adult_dose':d.adult_dose,'child_dose':d.child_dose,'frequency':d.frequency,'duration':d.duration,'notes':d.notes} for d in db.query(Drug).all()])

@app.route('/api/drugs/manage', methods=['POST','DELETE'])
@login_required
def manage_drugs():
    db = get_db()
    if request.method == 'POST':
        d = request.json
        db.add(Drug(trade_name=d['trade_name'], category=d['category'], generic_name=d.get('generic_name',''), adult_dose=d.get('adult_dose',''), child_dose=d.get('child_dose',''), frequency='1x3', duration='5 days'))
        db.commit()
        return jsonify({'status':'ok'})
    elif request.method == 'DELETE':
        db.query(Drug).filter_by(id=request.args.get('id')).delete()
        db.commit()
        return jsonify({'status':'ok'})

@app.route('/api/reload-drugs', methods=['POST'])
@login_required
def reload_drugs():
    if not current_user.is_admin:
        return jsonify({'error':'Unauthorized'}), 403
    db = get_db()
    db.query(Drug).delete()
    from data.drug_database import ALL_DRUGS
    for d in ALL_DRUGS:
        db.add(Drug(**d))
    db.commit()
    return jsonify({'status':'ok', 'count': len(ALL_DRUGS)})

# API Patients
@app.route('/api/patients', methods=['GET','POST'])
@login_required
def patients():
    db = get_db()
    if request.method == 'POST':
        d = request.json
        p = Patient(name=d['name'], age=d.get('age'), gender=d.get('gender'), phone=d.get('phone'), weight=d.get('weight'), chronic_diseases=d.get('chronic_diseases'), allergies=d.get('allergies'), chronic_drugs=d.get('chronic_drugs'), doctor_id=current_user.id)
        db.add(p); db.commit()
        return jsonify({'status':'ok', 'id':p.id}), 201
    return jsonify([{'id':p.id,'name':p.name,'age':p.age,'gender':p.gender,'phone':p.phone,'weight':p.weight,'chronic_diseases':p.chronic_diseases,'chronic_drugs':p.chronic_drugs,'allergies':p.allergies} for p in db.query(Patient).filter_by(doctor_id=current_user.id).all()])

@app.route('/api/patients/<int:pid>', methods=['PUT','DELETE'])
@login_required
def patient_update_delete(pid):
    db = get_db()
    p = db.query(Patient).filter_by(id=pid, doctor_id=current_user.id).first()
    if not p:
        return jsonify({'error': 'Patient not found'}), 404
    if request.method == 'PUT':
        data = request.json
        p.name = data.get('name', p.name)
        p.age = data.get('age', p.age)
        p.gender = data.get('gender', p.gender)
        p.phone = data.get('phone', p.phone)
        p.weight = data.get('weight', p.weight)
        p.chronic_diseases = data.get('chronic_diseases', p.chronic_diseases)
        p.allergies = data.get('allergies', p.allergies)
        p.chronic_drugs = data.get('chronic_drugs', p.chronic_drugs)
        db.commit()
        return jsonify({'status':'updated'})
    elif request.method == 'DELETE':
        db.delete(p)
        db.commit()
        return jsonify({'status':'deleted'})

# API AI, PDF, WhatsApp, Prescriptions, Emergencies, Interactions, Dosing
@app.route('/api/ai/analyze', methods=['POST'])
@login_required
def ai():
    from utils.gemini_helper import analyze_case
    d = request.json
    result = analyze_case(d['symptoms'], d.get('age',''), d.get('gender',''), d.get('chronic',''), d.get('allergies',''))
    return jsonify({'result': result})

@app.route('/api/generate-pdf', methods=['POST'])
@login_required
def pdf():
    try:
        d = request.json
        db = get_db()
        user = db.query(User).get(current_user.id)
        doctor = {'name':user.doctor_name or user.username,'phone':user.doctor_phone or '','specialty':user.doctor_specialty or '','clinic':user.clinic_name or 'Dental Clinic','address':user.clinic_address or '','logo':user.logo_path,'watermark':user.watermark_path}
        pdf_bytes = generate_pdf_bytes(d.get('patient',{}), d.get('drugs',[]), d.get('diagnosis',''), d.get('notes',''), doctor)
        return Response(pdf_bytes, mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=rx.pdf'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/whatsapp-link', methods=['POST'])
@login_required
def whatsapp():
    d = request.json
    phone = d.get('phone','').replace('+','').replace(' ','')
    name = d.get('name','Patient')
    msg = f"Dear {name}, your prescription from Dr. {current_user.doctor_name or 'Doctor'}."
    return jsonify({'link': f"https://wa.me/{phone}?text={urllib.parse.quote(msg)}"})

@app.route('/api/prescriptions', methods=['GET','POST'])
@login_required
def prescriptions():
    db = get_db()
    if request.method == 'POST':
        d = request.json
        rx = Prescription(patient_id=d.get('patient_id'), doctor_id=current_user.id, diagnosis=d.get('diagnosis'), items_json=json.dumps(d['drugs']), is_ready=d.get('is_ready',False), ready_name=d.get('ready_name',''))
        if current_user.is_admin and d.get('is_global'): rx.is_global_template = True
        db.add(rx); db.commit()
        return jsonify({'status':'ok'})
    q = db.query(Prescription).filter_by(is_ready=True)
    if not current_user.is_admin: q = q.filter((Prescription.doctor_id == current_user.id) | (Prescription.is_global_template == True))
    return jsonify([{'id':rx.id,'ready_name':rx.ready_name,'items_json':rx.items_json,'is_global_template':rx.is_global_template} for rx in q.all()])

@app.route('/api/emergencies')
@login_required
def emergencies():
    return jsonify([{'id':e.id,'name':e.name,'symptoms':e.symptoms,'procedure':e.procedure,'medications':e.medications} for e in get_db().query(EmergencyProtocol).all()])

@app.route('/api/check-interactions', methods=['POST'])
@login_required
def api_check_interactions():
    d = request.json
    warnings = []
    if d.get('patient_id'):
        p = get_db().query(Patient).get(int(d['patient_id']))
        if p:
            cd = [x.strip() for x in p.chronic_drugs.split(',') if x.strip()] if p.chronic_drugs else []
            di = [x.strip() for x in p.chronic_diseases.split(',') if x.strip()] if p.chronic_diseases else []
            warnings = check_interactions(d['drug_name'], cd, di)
    return jsonify({'warnings': warnings})

@app.route('/api/auto-dose', methods=['POST'])
@login_required
def api_auto_dose():
    d = request.json
    return jsonify(auto_adjust_dose(d['drug'], d.get('age',30), d.get('weight')))

@app.route('/api/admin/users', methods=['GET','POST','PUT','DELETE'])
@login_required
def admin_users():
    if not current_user.is_admin: return jsonify({'error':'Unauthorized'}), 403
    db = get_db()
    if request.method == 'GET':
        return jsonify([{'id':u.id,'username':u.username,'is_admin':u.is_admin,'is_active':u.is_active,'doctor_name':u.doctor_name} for u in db.query(User).all()])
    elif request.method == 'POST':
        d = request.json
        db.add(User(username=d['username'], password_hash=generate_password_hash(d['password'])))
        db.commit(); return jsonify({'status':'ok'})
    elif request.method == 'PUT':
        d = request.json; u = db.query(User).get(d['id'])
        if u and u.id != current_user.id:
            u.is_active = d.get('is_active', u.is_active)
            db.commit()
        return jsonify({'status':'ok'})
    elif request.method == 'DELETE':
        u = db.query(User).get(request.args.get('id'))
        if u and u.id != current_user.id: db.delete(u); db.commit()
        return jsonify({'status':'ok'})

@app.route('/api/settings', methods=['GET','POST'])
@login_required
def settings():
    db = get_db()
    if request.method == 'POST':
        data = request.json
        user = db.query(User).get(current_user.id)
        # هنا الإصلاح: استخدام أسماء الحقول الصحيحة التي ترسلها الواجهة
        if 'name' in data: user.doctor_name = data['name']
        if 'phone' in data: user.doctor_phone = data['phone']
        if 'specialty' in data: user.doctor_specialty = data['specialty']
        if 'clinic' in data: user.clinic_name = data['clinic']
        if 'address' in data: user.clinic_address = data['address']
        if 'password' in data and data['password']:
            user.password_hash = generate_password_hash(data['password'])
        db.commit()
        return jsonify({'status':'ok'})
    u = db.query(User).get(current_user.id)
    return jsonify({
        'name': u.doctor_name,
        'phone': u.doctor_phone,
        'specialty': u.doctor_specialty,
        'clinic': u.clinic_name,
        'address': u.clinic_address,
        'logo': u.logo_path,
        'photo': u.photo_path,
        'watermark': u.watermark_path
    })

@app.route('/api/upload-logo', methods=['POST'])
@login_required
def upload_logo():
    file = request.files.get('logo')
    if file:
        fname = f"logo_{current_user.id}.png"
        file.save(os.path.join(UPLOAD_FOLDER, fname))
        db = get_db()
        db.query(User).filter_by(id=current_user.id).update({'logo_path': f'/uploads/{fname}'})
        db.commit()
        return jsonify({'status':'ok', 'path': f'/uploads/{fname}'})
    return jsonify({'error':'no file'}), 400

@app.route('/api/upload-watermark', methods=['POST'])
@login_required
def upload_watermark():
    file = request.files.get('watermark')
    if file:
        fname = f"wm_{current_user.id}.png"
        file.save(os.path.join(UPLOAD_FOLDER, fname))
        db = get_db()
        db.query(User).filter_by(id=current_user.id).update({'watermark_path': f'/uploads/{fname}'})
        db.commit()
        return jsonify({'status':'ok', 'path': f'/uploads/{fname}'})
    return jsonify({'error':'no file'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
