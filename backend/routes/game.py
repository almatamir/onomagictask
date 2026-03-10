import threading
from flask import Blueprint, jsonify, request
from services.database import get_random_country, save_country, count_countries_left, get_existing_country_names, count_all_countries, reset_played
from services.gemini import generate_multiple_countries

game_bp = Blueprint('game', __name__)

MAX_COUNTRIES = 300
REFILL_THRESHOLD = 30
REFILL_AMOUNT = 20
is_refilling = False

def should_refill():
    return count_countries_left() < REFILL_THRESHOLD and not is_refilling

def refill_countries():
    global is_refilling
    is_refilling = True
    total = count_all_countries()
    if total < MAX_COUNTRIES:
        amount = min(REFILL_AMOUNT, MAX_COUNTRIES - total)
        existing_names = get_existing_country_names()
        new_countries = generate_multiple_countries(amount, existing_names)
        for country in new_countries:
            save_country(country)
    is_refilling = False

@game_bp.route('/country', methods=['GET'])
def get_country():
    country = get_random_country()
    if not country:
        return jsonify({'error': 'No countries available'}), 500
    return jsonify({'clues': country['clues'], 'id': country['name']})

@game_bp.route('/guess', methods=['POST'])
def check_guess():
    data = request.get_json()
    user_guess = data.get('guess', '').strip().lower()
    country_id = data.get('id', '').strip().lower()
    correct = user_guess == country_id

    if should_refill():
        threading.Thread(target=refill_countries).start()

    return jsonify({'correct': correct, 'message': 'Correct! 🎉' if correct else f'Wrong! The correct answer is {country_id.title()}'})

@game_bp.route('/reset', methods=['POST'])
def reset():
    reset_played()
    return jsonify({'message': 'Reset successful'})