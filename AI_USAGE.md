# AI Usage Documentation

## Tool Used
**Claude (Anthropic)** - via claude.ai

---

## How I Used AI

I used Claude as a thinking partner throughout the project.
Rather than asking for complete solutions, I led the planning process
and made all the key decisions myself.

---

## Example Prompts

**Deciding on the database strategy:**
> "I want to save 30 countries in MongoDB as a backup in case the API key runs out."

Claude explained the fallback pattern. I decided to pre-seed
30 countries instead of relying only on Gemini.

**Backend endpoints:**
> "Write a Flask endpoint GET /api/country that fetches from MongoDB."

Claude generated the basic route. I reviewed the logic and decisions.

**Frontend:**
> "Create a simple Next.js page with Tailwind that shows 3 clues
> and a text input for guessing. Keep it clean, no over-design."

Claude generated the component. I asked to simplify -
removing separate component files and keeping everything in one page.

**Debugging MongoDB SSL:**
> "I'm getting SSL certificate errors connecting to MongoDB on Mac, how do I fix this?"

Claude suggested the certifi fix. I applied it to both `database.py` and `seed.py`.

**Smart prefetching:**
> "I want the backend to automatically generate new countries from Gemini
> when the unplayed count drops below 20."

I came up with the prefetching concept. Claude helped implement
the `is_refilling` flag to prevent duplicate API calls, the `played` field
in MongoDB to track shown countries, and the bulk generation prompt.

**Gemini bulk generation:**
> "I don't want to call Gemini once per country - I want to request
> 15 countries in a single prompt."

I identified the inefficiency. Claude updated the prompt to return
a JSON array of countries in one call.

**Session reset:**
> "Every time a user opens the site, reset all played countries so they start fresh."

I decided on option 1 (global reset) over per-user sessions to keep it simple.
Claude implemented the /api/reset endpoint and the useEffect call in the frontend.

---

## What AI Generated
- `backend/app.py` - Flask server setup, blueprint registration
- `backend/routes/game.py` - GET /api/country, POST /api/guess, POST /api/reset endpoints
- `backend/services/database.py` - MongoDB connection
- `backend/services/gemini.py` - API call to generate countries
- `backend/seed.py` - one-time script to seed 30 countries into MongoDB
- `frontend/app/page.tsx` - game UI, display, screen with score, session reset on page load

---