import os
from groq import Groq

def analyze_case(symptoms, age, gender, chronic, allergies):
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        return "AI Error: API key not configured in Render."
    
    try:
        client = Groq(api_key=api_key)
        prompt = f"""You are a dental specialist. Analyze this case:
Symptoms: {symptoms}
Age: {age}, Gender: {gender}
Chronic conditions: {chronic or 'none'}
Allergies: {allergies or 'none'}

Provide:
1. Possible Diagnoses (2-3)
2. Most Likely Diagnosis
3. Recommended Medications (specific names, doses, duration)
4. Precautions & Warnings"""

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"
