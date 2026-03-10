from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random
import certifi

load_dotenv()

client = None
db = None

def init_db():
    global client, db
    client = MongoClient(os.getenv('MONGODB_URI'), tlsCAFile=certifi.where())
    db = client['onomagictask']
    print("Connected to MongoDB!")

def get_random_country():
    countries = list(db.countries.find({}, {'_id': 0}))
    if not countries:
        return None
    return random.choice(countries)

def save_country(country_data):

    existing = db.countries.find_one({'name': country_data['name']})
    if not existing:
        db.countries.insert_one(country_data)