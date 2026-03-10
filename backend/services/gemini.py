import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()

def generate_multiple_countries(amount, existing_names):
    try:
        client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
        
        prompt = f"""
        Generate {amount} different countries with exactly 3 clues each.
        Each clue must be SHORT - maximum 8 words.
        Do NOT include any of these countries: {', '.join(existing_names)}
        Return ONLY a JSON array in this exact format, nothing else:
        [
            {{
                "name": "Country Name",
                "clues": ["Short clue 1", "Short clue 2", "Short clue 3"],
                "source": "gemini"
            }}
        ]
        Make sure all countries are different from each other.
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        text = response.text.strip()
        if '```' in text:
            text = text.split('```')[1]
            if text.startswith('json'):
                text = text[4:]
        
        countries = json.loads(text)
        for country in countries:
            country['name'] = country['name'].lower()
        return countries
        
    except Exception as e:
        print(f"Gemini error: {e}")
        return []