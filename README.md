# Guess The Country 🌍

A web application where users guess a country based on 3 clues.

## Live Demo
[https://prolific-empathy-production.up.railway.app]

## Tech Stack
- **Frontend:** Next.js + TypeScript + Tailwind CSS
- **Backend:** Python + Flask
- **Database:** MongoDB Atlas
- **AI:** Google Gemini API (with MongoDB fallback)

## How to Run

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed.py
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

### backend/.env
```
MONGODB_URI=your_mongodb_connection_string
GEMINI_API_KEY=your_gemini_api_key
```

### frontend/.env.local
```
NEXT_PUBLIC_API_URL=http://127.0.0.1:5000
```

## How It Works
1. The app displays 3 clues about a random country
2. The user types their guess and submits
3. The app responds with correct or wrong + the correct answer
4. Click "Next Country" to play again

## Smart Prefetching
The backend tracks which countries have been shown (`played: true`).
When fewer than 40 unplayed countries remain, Gemini automatically
generates 20 new countries in a single API call and saves them to MongoDB.
Gemini receives the list of existing countries to avoid duplicates.
If Gemini is unavailable, the app continues using the pre-seeded dataset.
On each page load, all countries are reset so every user starts fresh.
New countries from Gemini always start with played: false.
The database is capped at 300 countries to prevent unlimited growth.