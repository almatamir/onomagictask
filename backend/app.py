from flask import Flask
from flask_cors import CORS
from routes.game import game_bp
from services.database import init_db

app = Flask(__name__)
CORS(app)

init_db()

app.register_blueprint(game_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=5000)