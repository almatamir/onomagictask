from flask import Blueprint, jsonify, request
from services.database import get_random_country, save_country
from services.gemini import generate_country

game_bp = Blueprint('game', __name__)

@game_bp.route('/country', methods=['GET'])
def get_country():
    country = get_random_country()
    
    if not country:
        country = generate_country()
        
        if not country:
            return jsonify({'error': 'No countries available'}), 500
        
        save_country(country)
    
    return jsonify({
        'clues': country['clues'],
        'id': country['name']
    })

@game_bp.route('/guess', methods=['POST'])
def check_guess():
    data = request.get_json()
    user_guess = data.get('guess', '').strip().lower()
    country_id = data.get('id', '').strip().lower()
    
    if user_guess == country_id:
        return jsonify({
            'correct': True,
            'message': 'Correct! 🎉'
        })
    else:
        return jsonify({
            'correct': False,
            'message': f'Wrong! The correct answer is {country_id.title()}'
        })