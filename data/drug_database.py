ALL_DRUGS = [
    # =====================================================================
    # 1. ANTIBIOTICS (المضادات الحيوية)
    # =====================================================================
    # --- IV / Injection ---
    {"trade_name":"Ceftriaxone + Sulbactam 1.5g IV","generic_name":"Ceftriaxone + Sulbactam","category":"Antibiotics","admin_route":"IV","adult_dose":"1.5 g","child_dose":"N/A","frequency":"1x1","duration":"3 days"},
    {"trade_name":"Unictam 375mg Vial IV","generic_name":"Unictam","category":"Antibiotics","admin_route":"IV","adult_dose":"375 mg","child_dose":"N/A","frequency":"1x1 or 1x2","duration":""},
    {"trade_name":"Unictam 750mg Vial IV","generic_name":"Unictam","category":"Antibiotics","admin_route":"IV","adult_dose":"750 mg","child_dose":"N/A","frequency":"1x1 or 1x2","duration":""},
    {"trade_name":"Unictam 1.5g Vial IV","generic_name":"Unictam","category":"Antibiotics","admin_route":"IV","adult_dose":"1.5 g","child_dose":"N/A","frequency":"1x1 or 1x2","duration":""},
    {"trade_name":"Unictam 3g Vial IV","generic_name":"Unictam","category":"Antibiotics","admin_route":"IV","adult_dose":"3 g","child_dose":"N/A","frequency":"1x1 or 1x2","duration":""},
    {"trade_name":"Ciplacef 500mg IV","generic_name":"Ciplacef","category":"Antibiotics","admin_route":"IV","adult_dose":"500 mg","child_dose":"N/A","frequency":"1x2","duration":"2 days"},
    {"trade_name":"Ciplacef 1000mg IV","generic_name":"Ciplacef","category":"Antibiotics","admin_route":"IV","adult_dose":"1000 mg","child_dose":"N/A","frequency":"1x2","duration":"2 days"},
    {"trade_name":"Dexamethasone 8mg Amp IV","generic_name":"Dexamethasone","category":"Antibiotics","admin_route":"IV","adult_dose":"8 mg","child_dose":"N/A","frequency":"1x1 or 1x2","duration":""},

    # --- Tablets / Capsules ---
    {"trade_name":"Augmentin 1gm Tab","generic_name":"Amoxicillin+Clavulanic Acid","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"1 g","child_dose":"N/A","frequency":"1x2","duration":"5-7 days"},
    {"trade_name":"Hibiotic 1gm Tab","generic_name":"Amoxicillin+Clavulanic Acid","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"1 g","child_dose":"N/A","frequency":"1x2","duration":"4 days"},
    {"trade_name":"Flagyl 500mg Tab","generic_name":"Metronidazole","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"200mg/5ml susp","frequency":"1x3","duration":"5-7 days"},
    {"trade_name":"Flomax 500mg Tab","generic_name":"Metronidazole","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"N/A","frequency":"1x3","duration":"5-7 days"},
    {"trade_name":"Amoxicillin 500mg Caps","generic_name":"Amoxicillin","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"250mg/5ml syrup","frequency":"1x3","duration":"5-7 days"},
    {"trade_name":"Keflex 250mg Tab","generic_name":"Cephalexin","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"250 mg","child_dose":"N/A","frequency":"1x2","duration":"2-3 days"},
    {"trade_name":"Keflex 500mg Tab","generic_name":"Cephalexin","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"250mg/5ml syrup","frequency":"1x3","duration":"5-7 days"},
    {"trade_name":"Azithromycin 500mg Tab","generic_name":"Azithromycin","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"200mg/5ml syrup","frequency":"1x1","duration":"3 days"},
    {"trade_name":"Clarithromycin 500mg Tab","generic_name":"Clarithromycin","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"N/A","frequency":"1x2","duration":"5-7 days"},
    {"trade_name":"Spiragyl Fort 500mg Tab","generic_name":"Spiramycin+Metronidazole","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Spirazole Fort 500mg Tab","generic_name":"Spiramycin+Metronidazole","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Ciprofloxacin 500mg Caps","generic_name":"Ciprofloxacin","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"N/A","frequency":"1x2","duration":"5-7 days"},
    {"trade_name":"Tetracycline 250mg Caps","generic_name":"Tetracycline","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"250 mg","child_dose":"N/A","frequency":"1x3","duration":"5-7 days","notes":"Before meal"},
    {"trade_name":"Doxycycline 100mg Caps","generic_name":"Doxycycline","category":"Antibiotics","admin_route":"Tab/Cap","adult_dose":"100 mg","child_dose":"N/A","frequency":"1x2 then 1x1","duration":"8 days"},

    # --- Suspension / Syrup (Children) ---
    {"trade_name":"Amoxicillin 125mg/5ml Susp","generic_name":"Amoxicillin","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"125mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Amoxicillin 250mg/5ml Susp","generic_name":"Amoxicillin","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"250mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Flumox 125mg/5ml Susp","generic_name":"Amoxicillin","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"125mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Flumox 250mg/5ml Susp","generic_name":"Amoxicillin","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"250mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Farcozol 250mg/5ml Susp","generic_name":"Farcozol","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"250mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Farcozol 500mg/5ml Susp","generic_name":"Farcozol","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"500mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Amrizole 250mg/5ml Susp","generic_name":"Metronidazole","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"250mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Amrizole 500mg/5ml Susp","generic_name":"Metronidazole","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"500mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Flagyl 125mg/5ml Susp","generic_name":"Metronidazole","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"125mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Flagyl 200mg/5ml Susp","generic_name":"Metronidazole","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"200mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Clavimox 312mg/5ml Susp","generic_name":"Amoxicillin+Clavulanic","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"312mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Clavimox 457mg/5ml Susp","generic_name":"Amoxicillin+Clavulanic","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"457mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Augmentin 156mg/5ml Susp","generic_name":"Amoxicillin+Clavulanic","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"156mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Augmentin 312mg/5ml Susp","generic_name":"Amoxicillin+Clavulanic","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"312mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Augmentin 457mg/5ml Susp","generic_name":"Amoxicillin+Clavulanic","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"457mg/5ml","frequency":"1x3","duration":"7 days"},
    {"trade_name":"Augmentin 625mg/5ml Susp","generic_name":"Amoxicillin+Clavulanic","category":"Antibiotics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"625mg/5ml","frequency":"1x3","duration":"7 days"},

    # =====================================================================
    # 2. ANTIFUNGAL & ULCER DRUGS (مضادات الفطريات وقرح الفم)
    # =====================================================================
    {"trade_name":"Tantum Verde M.W + Tetracycline 250mg","generic_name":"Benzydamine+Tetracycline","category":"Antifungals","admin_route":"Mouthwash","adult_dose":"5 ml","child_dose":"N/A","frequency":"x4","duration":"","notes":"Minor ulcers"},
    {"trade_name":"Epirelefan Amp + Phenadone Syrup + Saline","generic_name":"Epirelefan","category":"Antifungals","admin_route":"IV","adult_dose":"5 ml","child_dose":"N/A","frequency":"x4","duration":"","notes":"Major/immunity ulcers"},
    {"trade_name":"Oracure Gel","generic_name":"Oracure","category":"Antifungals","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"1x4","duration":"5-7 days"},
    {"trade_name":"Sperience Sachets","generic_name":"Sperience","category":"Antifungals","admin_route":"Topical","adult_dose":"1 sachet","child_dose":"N/A","frequency":"1x1","duration":""},
    {"trade_name":"Nystatin Oral Susp","generic_name":"Nystatin","category":"Antifungals","admin_route":"Susp/Syrup","adult_dose":"5 ml","child_dose":"4 drops","frequency":"X4","duration":"10-14 days","notes":"Rinse 2 min then swallow"},
    {"trade_name":"Nystatin Cream","generic_name":"Nystatin","category":"Antifungals","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"X4","duration":""},
    {"trade_name":"Daktarin 2% Oral Gel","generic_name":"Miconazole","category":"Antifungals","admin_route":"Topical","adult_dose":"2.5 ml","child_dose":"1.25 ml","frequency":"4 times/day","duration":"2 weeks"},
    {"trade_name":"Miconazole 2% Oral Gel","generic_name":"Miconazole","category":"Antifungals","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"4 times/day","duration":"2 weeks"},
    {"trade_name":"Mycostatin Drops","generic_name":"Nystatin","category":"Antifungals","admin_route":"Susp/Syrup","adult_dose":"1 ml","child_dose":"4 drops","frequency":"4x daily","duration":"10-14 days"},

    # =====================================================================
    # 3. ANTIVIRAL (مضادات الفيروسات)
    # =====================================================================
    {"trade_name":"Acyclovir 200mg Tab","generic_name":"Acyclovir","category":"Antivirals","admin_route":"Tab/Cap","adult_dose":"200 mg","child_dose":"N/A","frequency":"X5","duration":"7-10 days"},
    {"trade_name":"Acyclovir 400mg Tab","generic_name":"Acyclovir","category":"Antivirals","admin_route":"Tab/Cap","adult_dose":"400 mg","child_dose":"N/A","frequency":"1X2","duration":"7-10 days"},
    {"trade_name":"Zovirax 400mg Tab","generic_name":"Acyclovir","category":"Antivirals","admin_route":"Tab/Cap","adult_dose":"400 mg","child_dose":"N/A","frequency":"1X2","duration":"7-10 days"},
    {"trade_name":"Eaclovir 500mg Tab","generic_name":"Acyclovir","category":"Antivirals","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"N/A","frequency":"1X2","duration":"7-10 days"},
    {"trade_name":"Zovirax 5% Topical Cream","generic_name":"Acyclovir Topical","category":"Antivirals","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"5x daily","duration":"4-5 days"},
    {"trade_name":"Docosanol Cream","generic_name":"Docosanol","category":"Antivirals","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"5x daily","duration":"10 days"},
    {"trade_name":"Zovirax 200mg Susp","generic_name":"Acyclovir","category":"Antivirals","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"3 ml","frequency":"1X5","duration":"7-10 days"},
    {"trade_name":"Valtrex 1gm Tab","generic_name":"Valacyclovir","category":"Antivirals","admin_route":"Tab/Cap","adult_dose":"1 g","child_dose":"N/A","frequency":"1x2","duration":"10 days"},

    # =====================================================================
    # 4. ANALGESIC (المسكنات)
    # =====================================================================
    # --- Ampules / Injections ---
    {"trade_name":"Paracetamol 300mg/2ml IV","generic_name":"Paracetamol","category":"Analgesics","admin_route":"IV","adult_dose":"300 mg/2ml","child_dose":"N/A","frequency":"1x2","duration":"2 days"},
    {"trade_name":"Ketolac 30mg Amp","generic_name":"Ketorolac","category":"Analgesics","admin_route":"IV/IM","adult_dose":"30 mg","child_dose":"N/A","frequency":"1x2","duration":"2 days"},
    {"trade_name":"Cataflam 75mg Amp","generic_name":"Diclofenac","category":"Analgesics","admin_route":"IV/IM","adult_dose":"75 mg","child_dose":"N/A","frequency":"1x2","duration":"2 days"},
    {"trade_name":"Ketolac + Dexa Amp","generic_name":"Ketorolac+Dexamethasone","category":"Analgesics","admin_route":"IV/IM","adult_dose":"30mg+8mg","child_dose":"N/A","frequency":"1x2","duration":"2 days"},
    {"trade_name":"Voltarin 50mg Amp","generic_name":"Diclofenac","category":"Analgesics","admin_route":"IV/IM","adult_dose":"50 mg","child_dose":"N/A","frequency":"1x1 or 1x2","duration":"2 days"},
    {"trade_name":"Voltarin 75mg Amp","generic_name":"Diclofenac","category":"Analgesics","admin_route":"IV/IM","adult_dose":"75 mg","child_dose":"N/A","frequency":"1x1 or 1x2","duration":"2 days"},
    {"trade_name":"Voltarin 100mg Amp","generic_name":"Diclofenac","category":"Analgesics","admin_route":"IV/IM","adult_dose":"100 mg","child_dose":"N/A","frequency":"1x1 or 1x2","duration":"2 days"},

    # --- Tablets / Capsules ---
    {"trade_name":"Panadol 500mg Tab","generic_name":"Paracetamol","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"250mg/5ml syrup","frequency":"1x2","duration":"3 days"},
    {"trade_name":"Panadol 1gm Tab","generic_name":"Paracetamol","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"1 g","child_dose":"N/A","frequency":"1x2","duration":"3 days"},
    {"trade_name":"Brufen 200mg Tab","generic_name":"Ibuprofen","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"200 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Brufen 400mg Tab","generic_name":"Ibuprofen","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"400 mg","child_dose":"100mg/5ml syrup","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Brufen 600mg Tab","generic_name":"Ibuprofen","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"600 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Brufen 400mg + Panadol 500mg","generic_name":"Ibuprofen+Paracetamol","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"400+500 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Brufen 600mg + Novaldol 1gm","generic_name":"Ibuprofen+Paracetamol","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"600+1000 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Aspirin 100mg Tab","generic_name":"Aspirin","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"100 mg","child_dose":"N/A","frequency":"1x3/2","duration":"3 days"},
    {"trade_name":"Excedrin 200mg Tab","generic_name":"Aspirin+Paracetamol+Caffeine","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"200 mg","child_dose":"N/A","frequency":"1x2","duration":"3 days"},
    {"trade_name":"Diclofenac S.R 100mg Tab","generic_name":"Diclofenac","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"100 mg","child_dose":"N/A","frequency":"1x2","duration":"7 days"},
    {"trade_name":"Cataflam 25mg Tab","generic_name":"Diclofenac Potassium","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"25 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Cataflam 50mg Tab","generic_name":"Diclofenac Potassium","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"50 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Catafast 25mg Tab","generic_name":"Diclofenac Potassium","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"25 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Catafast 50mg Tab","generic_name":"Diclofenac Potassium","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"50 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Profen 400mg + Paracetamol 500mg","generic_name":"Ibuprofen+Paracetamol","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"400+500 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Naproxen S 440mg + Paracetamol 500mg","generic_name":"Naproxen+Paracetamol","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"440+500 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Dentaforce Cap","generic_name":"Dentaforce","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"1 cap","child_dose":"N/A","frequency":"1x3","duration":"4 days"},
    {"trade_name":"Naproxen 250mg Tab","generic_name":"Naproxen","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"250 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Naproxen 500mg Tab","generic_name":"Naproxen","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Hepamol 250mg Tab","generic_name":"Paracetamol","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"250 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Hepamol 500mg Tab","generic_name":"Paracetamol","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Cetafen Plus","generic_name":"Ibuprofen+Paracetamol+Caffeine","category":"Analgesics","admin_route":"Tab/Cap","adult_dose":"400+500+65 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},

    # --- Syrup / Suspension ---
    {"trade_name":"Paracetamol 100mg Syrup","generic_name":"Paracetamol","category":"Analgesics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"100mg/5ml","frequency":"1x3","duration":"5 days"},
    {"trade_name":"Adol 100mg Syrup","generic_name":"Paracetamol","category":"Analgesics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"100mg/5ml","frequency":"1x3","duration":"5 days"},
    {"trade_name":"Brufen 100mg/5ml Susp","generic_name":"Ibuprofen","category":"Analgesics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"100mg/5ml","frequency":"1x3","duration":"4 days"},
    {"trade_name":"Catafly 100mg/5ml Susp","generic_name":"Ibuprofen","category":"Analgesics","admin_route":"Susp/Syrup","adult_dose":"N/A","child_dose":"100mg/5ml","frequency":"1x3","duration":"4 days"},

    # =====================================================================
    # 5. HEMOSTATIC (موقفات النزيف)
    # =====================================================================
    {"trade_name":"Amri-K 10mg Amp","generic_name":"Vitamin K","category":"Hemostatic","admin_route":"IV","adult_dose":"10 mg","child_dose":"N/A","frequency":"1x1","duration":"2 days before & after surgery"},
    {"trade_name":"Kapron 500mg/5ml Amp","generic_name":"Tranexamic Acid","category":"Hemostatic","admin_route":"IV","adult_dose":"500 mg/5ml","child_dose":"N/A","frequency":"1x2","duration":""},
    {"trade_name":"Haemostop 500mg Amp","generic_name":"Tranexamic Acid","category":"Hemostatic","admin_route":"Local","adult_dose":"500 mg","child_dose":"N/A","frequency":"In gauze","duration":"","notes":"Local hemostatic"},

    # =====================================================================
    # 6. TRIPLE ANTIBIOTICS MIX (خلطة المضاد الثلاثية)
    # =====================================================================
    {"trade_name":"Triple Antibiotic Mix","generic_name":"Tetracycline+Ciprofloxacin+Metronidazole","category":"Triple Antibiotics Mix","admin_route":"Mix","adult_dose":"250+500+500 mg","child_dose":"N/A","frequency":"As directed","duration":"","notes":"Mix with saline/L.A"},

    # =====================================================================
    # 7. EMERGENCY CASES (حالات الطوارئ)
    # =====================================================================
    {"trade_name":"Adrenaline 1:1000","generic_name":"Epinephrine","category":"Emergency","admin_route":"IM/SC","adult_dose":"0.3-0.5 ml","child_dose":"0.15 ml","frequency":"Every 5 min","duration":"Max 3 doses","notes":"Anaphylaxis/Cardiac arrest/Asthma"},
    {"trade_name":"Solu-cortef 50mg Vial","generic_name":"Hydrocortisone","category":"Emergency","admin_route":"IV","adult_dose":"50 mg","child_dose":"N/A","frequency":"1-2 amp slowly","duration":"Once","notes":"Hypotension/Allergy"},
    {"trade_name":"Solu-cortef 100mg Vial","generic_name":"Hydrocortisone","category":"Emergency","admin_route":"IV","adult_dose":"100 mg","child_dose":"N/A","frequency":"1-2 amp slowly","duration":"Once"},
    {"trade_name":"Solu-cortef 200mg Vial","generic_name":"Hydrocortisone","category":"Emergency","admin_route":"IV","adult_dose":"200 mg","child_dose":"N/A","frequency":"1-2 amp slowly","duration":"Once"},
    {"trade_name":"Avil Amp","generic_name":"Pheniramine","category":"Emergency","admin_route":"IV/IM","adult_dose":"1 amp","child_dose":"0.5 mg/kg","frequency":"Once","duration":"Once","notes":"Allergy"},
    {"trade_name":"Neuril 10mg/2ml Amp IM","generic_name":"Diazepam","category":"Emergency","admin_route":"IM","adult_dose":"10 mg/2ml","child_dose":"N/A","frequency":"Once","duration":"Once","notes":"Seizures"},
    {"trade_name":"Nitroglycerine 5mg Sublingual","generic_name":"Nitroglycerin","category":"Emergency","admin_route":"Sublingual","adult_dose":"5 mg","child_dose":"N/A","frequency":"Every 5 min","duration":"Max 3 doses","notes":"Angina/MI"},
    {"trade_name":"Glucagen 1mg/ml Vial","generic_name":"Glucagon","category":"Emergency","admin_route":"IM/IV/SC","adult_dose":"1 mg/ml","child_dose":"N/A","frequency":"Once","duration":"Once","notes":"Hypoglycemic coma"},
    {"trade_name":"Capoten 25mg Sublingual","generic_name":"Captopril","category":"Emergency","admin_route":"Sublingual","adult_dose":"25 mg","child_dose":"N/A","frequency":"Once","duration":"Once","notes":"Hypertensive crisis"},
    {"trade_name":"Ventolin Inhaler","generic_name":"Albuterol","category":"Emergency","admin_route":"Inhalation","adult_dose":"2-3 puffs","child_dose":"1-2 puffs","frequency":"Every 20 min","duration":"Max 3 times"},

    # =====================================================================
    # 8. GEL (الجيل الموضعي)
    # =====================================================================
    {"trade_name":"Chlorhexidine Gel","generic_name":"Chlorhexidine","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"1x4","duration":"5-7 days"},
    {"trade_name":"Gengigel Forte Gel","generic_name":"Hyaluronic Acid","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"1x4","duration":"5-7 days"},
    {"trade_name":"Pervident Gel","generic_name":"Pervident","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"1x4","duration":"5-7 days"},
    {"trade_name":"Orasore Mouth Ulcer Gel","generic_name":"Orasore","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"1x4","duration":"5-7 days"},
    {"trade_name":"Lidocaine Gel 20%","generic_name":"Lidocaine","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"1x4","duration":"7 days"},
    {"trade_name":"Benzocaine 20% Gel","generic_name":"Benzocaine","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"1x4","duration":"7 days"},
    {"trade_name":"Fluoride Gel 0.9%","generic_name":"Sodium Fluoride","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"As directed","duration":""},
    {"trade_name":"Fluoride Gel 1.23%","generic_name":"Sodium Fluoride","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"As directed","duration":""},
    {"trade_name":"Fluocinonide Gel 0.05%","generic_name":"Fluocinonide","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"As directed","duration":""},
    {"trade_name":"Reparil Gel","generic_name":"Reparil","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"N/A","frequency":"1x3","duration":"","notes":"TMJ clicking/pain"},
    {"trade_name":"Perio Kin Gel","generic_name":"Hyaluronic Acid 1%","category":"Gel","admin_route":"Topical","adult_dose":"Apply","child_dose":"Apply","frequency":"As directed","duration":""},

    # =====================================================================
    # 9. MUSCLE RELAXANTS (باسطات العضلات)
    # =====================================================================
    {"trade_name":"Baclofen 10mg Tab","generic_name":"Baclofen","category":"Muscle Relaxants","admin_route":"Tab/Cap","adult_dose":"10 mg","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Dimra Tab","generic_name":"Dimra","category":"Muscle Relaxants","admin_route":"Tab/Cap","adult_dose":"1 tab","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Myofen Tab","generic_name":"Myofen","category":"Muscle Relaxants","admin_route":"Tab/Cap","adult_dose":"1 tab","child_dose":"N/A","frequency":"1x3","duration":"3 days"},
    {"trade_name":"Multi-Relax 10mg Tab","generic_name":"Multi-Relax","category":"Muscle Relaxants","admin_route":"Tab/Cap","adult_dose":"10 mg","child_dose":"N/A","frequency":"1x1","duration":"","notes":"Before sleep"},
    {"trade_name":"Myolgin","generic_name":"Orphenadrine+Paracetamol","category":"Muscle Relaxants","admin_route":"Tab/Cap","adult_dose":"1 tab","child_dose":"N/A","frequency":"1x3","duration":"5 days"},

    # =====================================================================
    # 10. MOUTH PREPARATION DRUGS (غسول ومستحضرات الفم)
    # =====================================================================
    {"trade_name":"Hexitol (CHX) M.W","generic_name":"Chlorhexidine","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"10 ml","frequency":"1x3","duration":"2 weeks"},
    {"trade_name":"Orovex (CHX + S.F) M.W","generic_name":"Chlorhexidine+Sodium Fluoride","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"10 ml","frequency":"1x3","duration":"2 weeks"},
    {"trade_name":"H2O2 30% M.W","generic_name":"Hydrogen Peroxide","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"N/A","frequency":"1x3","duration":"5 days"},
    {"trade_name":"Tantum Verde M.W","generic_name":"Benzydamine","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"5 ml","child_dose":"N/A","frequency":"x4","duration":"5 days"},
    {"trade_name":"Verolex M.W","generic_name":"Verolex","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"N/A","frequency":"1x4","duration":"7 days"},
    {"trade_name":"Oxymeria M.W","generic_name":"Oxymeria","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"N/A","frequency":"1x3","duration":""},
    {"trade_name":"BreathRx M.W","generic_name":"BreathRx","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"N/A","frequency":"1x3","duration":""},
    {"trade_name":"B-Fresh M.W","generic_name":"B-Fresh","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"N/A","frequency":"1x3","duration":"2 weeks","notes":"T.S"},
    {"trade_name":"Betadine M.W","generic_name":"Povidone-Iodine","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"10 ml","frequency":"1x3","duration":"10 days"},
    {"trade_name":"Corsodyl Mouthwash","generic_name":"Chlorhexidine 0.2%","category":"Mouth Prep","admin_route":"Mouthwash","adult_dose":"15 ml","child_dose":"10 ml","frequency":"1x2","duration":"7 days"},

    # =====================================================================
    # 11. TOOTH PASTE (معاجين الأسنان)
    # =====================================================================
    {"trade_name":"Signal Toothpaste","generic_name":"Signal","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x3","duration":"Daily","notes":"Anti caries"},
    {"trade_name":"Crest Toothpaste","generic_name":"Crest","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x3","duration":"Daily"},
    {"trade_name":"Sensodyne Fluoride","generic_name":"Sensodyne","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x3","duration":"Daily","notes":"Protection"},
    {"trade_name":"Close Up 120ml","generic_name":"Close Up","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x3","duration":"Daily","notes":"Freshness"},
    {"trade_name":"Parodontax Toothpaste","generic_name":"Parodontax","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x3","duration":"Daily","notes":"Inflamed gum"},
    {"trade_name":"Sensodyne Rapid Action","generic_name":"Sensodyne","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x2","duration":"Daily","notes":"Sensitivity"},
    {"trade_name":"Sensodyne Clinical White","generic_name":"Sensodyne","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x2","duration":"Daily","notes":"White teeth"},
    {"trade_name":"Signal Expert White","generic_name":"Signal","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x2","duration":"Daily","notes":"White teeth"},
    {"trade_name":"White Glo Toothpaste","generic_name":"White Glo","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x2","duration":"Daily"},
    {"trade_name":"Crest 3D White Fresh","generic_name":"Crest","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x2","duration":"Daily"},
    {"trade_name":"Signal Kids","generic_name":"Signal","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x3","duration":"Daily","notes":"Children"},
    {"trade_name":"Crest Kids","generic_name":"Crest","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x3","duration":"Daily","notes":"Children"},
    {"trade_name":"Colgate Kids","generic_name":"Colgate","category":"Tooth Paste","admin_route":"Paste","adult_dose":"Apply","child_dose":"Apply","frequency":"1x3","duration":"Daily","notes":"Children"},

    # =====================================================================
    # 12. VITAMINS (الفيتامينات)
    # =====================================================================
    {"trade_name":"Vit-C 500mg Cap","generic_name":"Vitamin C","category":"Vitamins","admin_route":"Tab/Cap","adult_dose":"500 mg","child_dose":"250 mg","frequency":"1x2","duration":""},
    {"trade_name":"Vit-C 1gm Cap","generic_name":"Vitamin C","category":"Vitamins","admin_route":"Tab/Cap","adult_dose":"1 g","child_dose":"N/A","frequency":"1x2","duration":""},
    {"trade_name":"Vit E 1gm Caps","generic_name":"Vitamin E","category":"Vitamins","admin_route":"Tab/Cap","adult_dose":"1 g","child_dose":"N/A","frequency":"1x1","duration":""},
    {"trade_name":"Vit-B Complex Cap","generic_name":"Vitamin B Complex","category":"Vitamins","admin_route":"Tab/Cap","adult_dose":"1 cap","child_dose":"N/A","frequency":"1x1","duration":""},
    {"trade_name":"Osteocare Cap","generic_name":"Calcium+D3+Mg+Zinc","category":"Vitamins","admin_route":"Tab/Cap","adult_dose":"1 cap","child_dose":"N/A","frequency":"1x1","duration":""},
    {"trade_name":"Omega 3 Plus Caps","generic_name":"Omega 3","category":"Vitamins","admin_route":"Tab/Cap","adult_dose":"1 cap","child_dose":"N/A","frequency":"1x1","duration":"30 days"},
    {"trade_name":"Multiple Vitamin Cap","generic_name":"Multivitamin","category":"Vitamins","admin_route":"Tab/Cap","adult_dose":"1 cap","child_dose":"N/A","frequency":"1x1","duration":"30 days"},
    {"trade_name":"Neurobion Tablets","generic_name":"B1+B6+B12","category":"Vitamins","admin_route":"Tab/Cap","adult_dose":"1 tab","child_dose":"N/A","frequency":"1x1","duration":"30 days"},

    # =====================================================================
    # 13. ANTI-EDEMATOUS (مضادات التورم)
    # =====================================================================
    {"trade_name":"α-Chymotrypsin Amp","generic_name":"Alpha-Chymotrypsin","category":"Steroids","admin_route":"IV","adult_dose":"1 amp","child_dose":"N/A","frequency":"1x2","duration":""},
    {"trade_name":"Alphintern Tab","generic_name":"Chymotrypsin","category":"Steroids","admin_route":"Tab/Cap","adult_dose":"1 tab","child_dose":"N/A","frequency":"1x3","duration":"4 days","notes":"Before meal"},
    {"trade_name":"Hemoclar Gel","generic_name":"Hemoclar","category":"Steroids","admin_route":"Topical","adult_dose":"Apply","child_dose":"N/A","frequency":"1x3","duration":""},
    {"trade_name":"Oradexon 8mg Tab","generic_name":"Dexamethasone","category":"Steroids","admin_route":"Tab/Cap","adult_dose":"8 mg","child_dose":"N/A","frequency":"1x1","duration":"3 days"},
    {"trade_name":"Ambezim Tab","generic_name":"Serratiopeptidase","category":"Steroids","admin_route":"Tab/Cap","adult_dose":"1 tab","child_dose":"N/A","frequency":"1x3","duration":"5 days"},

    # =====================================================================
    # 14. SEDATIVE (المهدئات)
    # =====================================================================
    {"trade_name":"Tegretol 200mg Tab","generic_name":"Carbamazepine","category":"Sedative","admin_route":"Tab/Cap","adult_dose":"200 mg","child_dose":"N/A","frequency":"1x1","duration":""},
    {"trade_name":"Amitriptine 50mg Caps","generic_name":"Amitriptyline","category":"Sedative","admin_route":"Tab/Cap","adult_dose":"50 mg","child_dose":"N/A","frequency":"1x1","duration":""},
    {"trade_name":"Diazepam 50mg Tab","generic_name":"Diazepam","category":"Sedative","admin_route":"Tab/Cap","adult_dose":"50 mg","child_dose":"N/A","frequency":"As needed","duration":""},
    {"trade_name":"Tramadol 50mg Tab","generic_name":"Tramadol","category":"Sedative","admin_route":"Tab/Cap","adult_dose":"50 mg","child_dose":"N/A","frequency":"As needed","duration":""},
]
