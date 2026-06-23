INTERACTIONS_DB = [
    {"drug":"Metronidazole","interacts_with":["Warfarin"],"severity":"Severe","desc":"يزيد مفعول الوارفارين"},
    {"drug":"Ibuprofen","interacts_with":["Warfarin"],"severity":"Severe","desc":"يزيد خطر النزيف"},
    {"drug":"Diclofenac","interacts_with":["Warfarin"],"severity":"Severe","desc":"يزيد خطر النزيف"},
    {"drug":"Tetracycline","interacts_with":["Warfarin"],"severity":"Severe","desc":"يزيد فعالية مضادات التخثر"},
    {"drug":"Ciprofloxacin","interacts_with":["Theophylline"],"severity":"Severe","desc":"يزيد سميته"},
    {"drug":"Fluconazole","interacts_with":["Warfarin"],"severity":"Severe","desc":"يزيد مفعول الوارفارين"},
]
DISEASE_CONTRAINDICATIONS = [
    {"disease":"Asthma","drug":"Ibuprofen","desc":"قد يسبب تشنج قصبي"},
    {"disease":"Asthma","drug":"Diclofenac","desc":"قد يسبب تشنج قصبي"},
    {"disease":"Peptic Ulcer","drug":"Ibuprofen","desc":"ممنوع لمرضى القرحة"},
    {"disease":"Peptic Ulcer","drug":"Diclofenac","desc":"ممنوع لمرضى القرحة"},
    {"disease":"Liver Disease","drug":"Metronidazole","desc":"يحتاج تعديل الجرعة"},
    {"disease":"Renal Impairment","drug":"Ibuprofen","desc":"تجنب في القصور الكلوي"},
    {"disease":"Cardiac Disease","drug":"Diclofenac","desc":"ممنوع لمرضى القلب"},
    {"disease":"Hypertension","drug":"Diclofenac","desc":"قد يرفع الضغط"},
    {"disease":"Pregnancy","drug":"Tetracycline","desc":"ممنوع في الحمل"},
    {"disease":"Pregnancy","drug":"Ibuprofen","desc":"ممنوع في الثلث الثالث"},
]
def check_interactions(drug_name, patient_drugs=None, patient_diseases=None):
    warnings = []
    patient_drugs = patient_drugs or []
    patient_diseases = patient_diseases or []
    drug_lower = drug_name.lower().strip()
    for item in INTERACTIONS_DB:
        if item["drug"].lower() in drug_lower:
            for existing in patient_drugs:
                for target in item["interacts_with"]:
                    if target.lower() in existing.lower():
                        warnings.append({"type":"drug","severity":item["severity"],"drug1":item["drug"],"drug2":target,"desc":item["desc"]})
            for disease in patient_diseases:
                for contra in DISEASE_CONTRAINDICATIONS:
                    if contra["drug"].lower() in drug_lower and contra["disease"].lower() in disease.lower():
                        warnings.append({"type":"disease","severity":"Moderate","drug":contra["drug"],"disease":contra["disease"],"desc":contra["desc"]})
    return warnings
def auto_adjust_dose(drug, age, weight=None):
    drug = drug.copy()
    age = int(age) if age else 30
    if age <= 12 and drug.get('child_dose') and drug['child_dose'] != 'N/A':
        drug['dosage'] = drug['child_dose']
        drug['note'] = f"Pediatric dose (age {age})"
    elif age >= 65:
        drug['note'] = "Geriatric: consider renal function"
    return drug
