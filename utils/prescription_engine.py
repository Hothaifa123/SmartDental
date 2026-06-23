from fpdf import FPDF
import os, datetime

class A5Rx(FPDF):
    def __init__(self, doctor=None):
        super().__init__(format='A5')
        self.doctor = doctor or {}
        arial = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Arial.ttf')
        if os.path.exists(arial):
            self.add_font('Arial', '', arial, uni=True)
            self.add_font('Arial', 'B', arial, uni=True)
            self.FONT = 'Arial'
        else:
            self.FONT = 'Helvetica'
        self.set_left_margin(10)
        self.set_right_margin(10)
        self.set_auto_page_break(True, 15)

    def header(self):
        logo = self.doctor.get('logo')
        if logo:
            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), logo.lstrip('/'))
            if os.path.exists(path):
                self.image(path, x=10, y=8, h=14)
        self.set_font(self.FONT, 'B', 11)
        self.cell(0, 6, self.doctor.get('name', 'Dr.'), ln=True, align='R')
        self.set_font(self.FONT, '', 8)
        self.cell(0, 4, f"Phone: {self.doctor.get('phone','')}  |  {self.doctor.get('specialty','')}", ln=True, align='R')
        addr = self.doctor.get('address','')
        if addr: self.cell(0, 4, addr, ln=True, align='R')
        self.ln(3)
        self.line(10, self.get_y(), self.w - 10, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-20)
        self.line(10, self.get_y(), self.w - 10, self.get_y())
        self.set_font(self.FONT, 'I', 8)
        self.cell(0, 6, "Signature: __________________", ln=True, align='R')
        self.set_font(self.FONT, '', 6)
        self.cell(0, 4, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}  |  {self.doctor.get('clinic','')}", ln=True, align='C')

def generate_pdf_bytes(patient=None, drugs=None, diagnosis="", notes="", doctor=None):
    try:
        pdf = A5Rx(doctor)
        pdf.add_page()
        wm = doctor.get('watermark') if doctor else None
        if wm:
            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), wm.lstrip('/'))
            if os.path.exists(path): pdf.image(path, x=20, y=50, w=pdf.w-40)
        p = patient or {}
        if any(p.get(k) for k in ['name','age','gender','phone']):
            pdf.set_font(pdf.FONT, 'B', 10)
            pdf.cell(0, 6, "Patient Info", ln=True)
            pdf.set_font(pdf.FONT, '', 9)
            pdf.cell(0, 5, f"Name: {p.get('name','')}    Age: {p.get('age','')}    Gender: {p.get('gender','')}", ln=True)
            parts = []
            if p.get('phone'): parts.append(f"Phone: {p['phone']}")
            if p.get('weight'): parts.append(f"Weight: {p['weight']}kg")
            if diagnosis: parts.append(f"Diagnosis: {diagnosis}")
            if parts: pdf.cell(0, 5, "    ".join(parts), ln=True)
            pdf.ln(3)
        drugs = drugs or []
        if drugs:
            pdf.set_font(pdf.FONT, 'B', 11)
            pdf.set_text_color(180,0,0)
            pdf.cell(0, 7, 'Rx:', ln=True)
            pdf.set_text_color(0,0,0)
            pdf.ln(2)
            size = 7 if len(drugs) > 10 else (8 if len(drugs) > 6 else 9)
            pdf.set_font(pdf.FONT, '', size)
            for d in drugs:
                line = f"- {d.get('drug_name','')}  {d.get('dosage','')}  {d.get('frequency','')}"
                if d.get('duration'): line += f"  for {d['duration']}"
                pdf.multi_cell(pdf.w - 24, 4.2, line)
                pdf.ln(0.5)
        if notes:
            pdf.ln(3)
            pdf.set_font(pdf.FONT, 'I', 8)
            pdf.multi_cell(0, 4, f"Notes: {notes}")
        return bytes(pdf.output())
    except Exception as e:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Helvetica', '', 10)
        pdf.cell(0, 10, f"Error: {str(e)}")
        return bytes(pdf.output())
