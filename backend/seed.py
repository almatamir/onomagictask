from backend.countries_data import countries
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

def seed_database():
    client = MongoClient(os.getenv('MONGODB_URI'), tlsCAFile=certifi.where())
    db = client['onomagictask']
    
    db.countries.delete_many({})
    db.countries.insert_many(countries)
    print(f"Successfully seeded {len(countries)} countries!")
    client.close()

if __name__ == '__main__':
    seed_database()