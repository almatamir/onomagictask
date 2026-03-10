# AI Usage Documentation

## Tool Used
**Claude (Anthropic)** - via claude.ai

---

## How I Used AI

I used Claude as a thinking partner throughout the project.
Rather than asking for complete solutions, I led the planning process and made all the key decisions myself.

---

## Example Prompts

**Planning the architecture:**
> "I want to build a Guess The Country app with Gemini API and MongoDB.
> Let's plan the architecture together before writing any code."

Claude suggested options, I chose Flask + Next.js and decided to combine
Python (which I know) with Next.js (which I wanted to learn).

**Deciding on the database strategy:**
> "I want to save 30 countries in MongoDB as a backup in case the API key runs out."

Claude explained the fallback pattern. I made the decision to pre-seed
30 countries instead of relying only on Gemini.

**Backend endpoints:**
> "Write a Flask endpoint GET /api/country that first tries Gemini,
> and falls back to MongoDB if it fails."

Claude generated the basic route. I then reviewed the logic and decided
to add the `?new=true` parameter so the frontend controls when to call Gemini.

**Frontend:**
> "Create a simple Next.js page with Tailwind that shows 3 clues
> and a text input for guessing. Keep it clean, no over-design."

Claude generated the component. I reviewed it and asked to simplify -
removing separate component files and keeping everything in one page.

**Debugging MongoDB SSL:**
> "I'm getting SSL certificate errors connecting to MongoDB on Mac, how do I fix this?"

Claude suggested the certifi fix. I applied it to both `database.py` and `seed.py`.

**Debugging Gemini:**

---

## What AI Generated
- `backend/app.py` - Flask server setup
- `backend/routes/game.py` - API endpoints
- `backend/services/database.py` - MongoDB connection
- `backend/services/gemini.py` - Gemini API integration
- `backend/seed.py` - 30 countries dataset
- `frontend/app/page.tsx` - Game UI

---

## What I Modified Myself
- Fixed MongoDB SSL certificate error on Mac
- Debugged and tested each endpoint manually in the browser
- Fixed git repository conflicts during initial setup
- Made all key architectural decisions throughout the process

---
