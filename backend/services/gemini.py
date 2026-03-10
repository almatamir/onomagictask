import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

def generate_country():
    # try:
    #     genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    #     model = genai.GenerativeModel('gemini-1.5-flash')
        
    #     prompt = """
    #     Generate a random country with exactly 3 clues.
    #     Return ONLY a JSON object in this exact format, nothing else:
    #     {
    #         "name": "Country Name",
    #         "clues": [
    #             "Clue 1 about the country",
    #             "Clue 2 about the country", 
    #             "Clue 3 about the country"
    #         ],
    #         "source": "gemini"
    #     }
    #     Make the clues interesting but not too easy.
    #     """
        
    #     response = model.generate_content(prompt)
    #     text = response.text.strip()
        
    #     if '```' in text:
    #         text = text.split('```')[1]
    #         if text.startswith('json'):
    #             text = text[4:]
        
    #     country = json.loads(text)
    #     return country
        
    # except Exception as e:
    #     print(f"Gemini error: {e}")
    #     return None

    return None