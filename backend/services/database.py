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
    countries = list(db.countries.find({'played': {'$ne': True}}, {'_id': 0}))
    if not countries:
        reset_played()
        countries = list(db.countries.find({'played': {'$ne': True}}, {'_id': 0}))
    country = random.choice(countries)
    db.countries.update_one({'name': country['name']}, {'$set': {'played': True}})
    return country

def save_country(country_data):
    existing = db.countries.find_one({'name': country_data['name']})
    if not existing:
        country_data['played'] = False
        db.countries.insert_one(country_data)

def count_countries_left():
   return db.countries.count_documents({'played': {'$ne': True}})

def get_existing_country_names():
    return [c['name'] for c in db.countries.find({}, {'name': 1, '_id': 0})]

def reset_played():
    db.countries.update_many({}, {'$set': {'played': False}})

def count_all_countries():
    return db.countries.count_documents({})