from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

countries = [
    {"name": "japan", "clues": ["Capital is Tokyo", "Famous for sushi and ramen", "Island nation in East Asia"], "source": "seed"},
    {"name": "brazil", "clues": ["Largest country in South America", "Famous for the Amazon rainforest", "Hosts the Rio Carnival"], "source": "seed"},
    {"name": "france", "clues": ["Capital is Paris", "Famous for the Eiffel Tower", "Known for wine and cheese"], "source": "seed"},
    {"name": "australia", "clues": ["Only country that is also a continent", "Home to kangaroos and koalas", "Sydney Opera House is here"], "source": "seed"},
    {"name": "egypt", "clues": ["Home to the ancient pyramids", "The Nile river flows through it", "Located in North Africa"], "source": "seed"},
    {"name": "canada", "clues": ["Second largest country in the world", "Famous for maple syrup", "Has two official languages"], "source": "seed"},
    {"name": "india", "clues": ["Most populous country in the world", "Home to the Taj Mahal", "Birthplace of yoga"], "source": "seed"},
    {"name": "italy", "clues": ["Home to the Roman Colosseum", "Famous for pizza and pasta", "Shaped like a boot"], "source": "seed"},
    {"name": "mexico", "clues": ["Famous for tacos and guacamole", "Home to ancient Mayan ruins", "Capital is Mexico City"], "source": "seed"},
    {"name": "china", "clues": ["Has the Great Wall", "Most populous country historically", "Capital is Beijing"], "source": "seed"},
    {"name": "greece", "clues": ["Birthplace of democracy", "Home to the Acropolis", "Famous for its islands and blue domes"], "source": "seed"},
    {"name": "argentina", "clues": ["Famous for tango dance", "Home to Patagonia", "Capital is Buenos Aires"], "source": "seed"},
    {"name": "russia", "clues": ["Largest country in the world", "Has Lake Baikal, the deepest lake", "Capital is Moscow"], "source": "seed"},
    {"name": "south africa", "clues": ["Has three capital cities", "Home to Nelson Mandela", "Famous for safari and wildlife"], "source": "seed"},
    {"name": "spain", "clues": ["Famous for flamenco dancing", "Home to the Sagrada Familia", "Capital is Madrid"], "source": "seed"},
    {"name": "thailand", "clues": ["Known as the Land of Smiles", "Famous for Pad Thai", "Home to many Buddhist temples"], "source": "seed"},
    {"name": "morocco", "clues": ["Located in North Africa", "Famous for its colorful medinas", "Capital is Rabat"], "source": "seed"},
    {"name": "peru", "clues": ["Home to Machu Picchu", "Famous for the Inca Empire", "Amazon river originates here"], "source": "seed"},
    {"name": "norway", "clues": ["Famous for the Northern Lights", "Land of fjords", "Capital is Oslo"], "source": "seed"},
    {"name": "kenya", "clues": ["Famous for the Maasai Mara safari", "Home to Mount Kilimanjaro region", "Capital is Nairobi"], "source": "seed"},
    {"name": "portugal", "clues": ["Famous for Fado music", "Discovered Brazil in 1500", "Capital is Lisbon"], "source": "seed"},
    {"name": "turkey", "clues": ["Located on two continents", "Home to the Hagia Sophia", "Capital is Ankara"], "source": "seed"},
    {"name": "new zealand", "clues": ["Filming location of Lord of the Rings", "Home to the Maori people", "Known for rugby and kiwi birds"], "source": "seed"},
    {"name": "colombia", "clues": ["Famous for its coffee", "Capital is Bogota", "Named after Christopher Columbus"], "source": "seed"},
    {"name": "sweden", "clues": ["Home to IKEA and Spotify", "Famous for the Nobel Prize", "Capital is Stockholm"], "source": "seed"},
    {"name": "indonesia", "clues": ["Largest archipelago in the world", "Home to the island of Bali", "Capital is Jakarta"], "source": "seed"},
    {"name": "germany", "clues": ["Famous for Oktoberfest", "Home to the Berlin Wall history", "Capital is Berlin"], "source": "seed"},
    {"name": "cuba", "clues": ["Famous for cigars and salsa music", "Largest island in the Caribbean", "Capital is Havana"], "source": "seed"},
    {"name": "iceland", "clues": ["Land of fire and ice", "Has more hot springs than any other country", "Capital is Reykjavik"], "source": "seed"},
    {"name": "nigeria", "clues": ["Most populous country in Africa", "Famous for Nollywood films", "Capital is Abuja"], "source": "seed"},
]

def seed_database():
    client = MongoClient(os.getenv('MONGODB_URI'), tlsCAFile=certifi.where())
    db = client['onomagictask']
    
    db.countries.delete_many({})
    db.countries.insert_many(countries)
    print(f"Successfully seeded {len(countries)} countries!")
    client.close()

if __name__ == '__main__':
    seed_database()