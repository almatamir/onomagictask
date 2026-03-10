# Guess The Country 🌍

A web application where users guess a country based on 3 clues.

## Tech Stack
- **Frontend:** Next.js + TypeScript + Tailwind CSS
- **Backend:** Python + Flask
- **Database:** MongoDB Atlas
- **AI:** Google Gemini API (fallback to MongoDB dataset)

## How to Run

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables
Create a `backend/.env` file:
```
MONGODB_URI=your_mongodb_connection_string
GEMINI_API_KEY=your_gemini_api_key
```

## How It Works
1. The app displays 3 clues about a random country
2. The user types their guess and submits
3. The app responds with correct/wrong + the answer
4. Click "Next Country" to play again

The backend first tries to generate a new country using Gemini API.
If Gemini is unavailable, it falls back to 30 pre-seeded countries in MongoDB.