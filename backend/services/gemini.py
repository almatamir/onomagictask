import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()

def generate_country():
    try:
        client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
        
        prompt = """
        Generate a random country with exactly 3 clues.
        Each clue must be SHORT: 4 - 10 words.
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
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        text = response.text.strip()
        
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