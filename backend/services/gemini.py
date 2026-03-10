import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

def generate_country():
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key={api_key}"
        
        prompt = """
        Generate a random country with exactly 3 clues.
        Return ONLY a JSON object in this exact format, nothing else:
        {
            "name": "Country Name",
            "clues": [
                "Clue 1 about the country",
                "Clue 2 about the country",
                "Clue 3 about the country"
            ],
            "source": "gemini"
        }
        Make the clues interesting but not too easy.
        """
        
        body = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        response = requests.post(url, json=body)
        response_json = response.json()
        print("Gemini response:", response_json)
        text = response_json['candidates'][0]['content']['parts'][0]['text'].strip()
        
        if '```' in text:
            text = text.split('```')[1]
            if text.startswith('json'):
                text = text[4:]
        
        country = json.loads(text)
        country['name'] = country['name'].lower()
        return country
        
    except Exception as e:
        print(f"Gemini error: {e}")
        return None