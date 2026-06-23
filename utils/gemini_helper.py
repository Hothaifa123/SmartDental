import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
def analyze_case(symptoms, age, gender, chronic, allergies):
    if not GEMINI_API_KEY: return "API key not configured."
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        prompt = f"""As a dental specialist, analyze: Symptoms: {symptoms}, Age: {age}, Gender: {gender}, Chronic: {chronic or 'none'}, Allergies: {allergies or 'none'}. Provide: 1. Possible Diagnoses 2. Recommended Medications 3. Precautions"""
        return model.generate_content(prompt).text
    except Exception as e:
        return f"AI Error: {str(e)}"
