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

**Planning the architecture:**
> "I want to build a Guess The Country app with Gemini API and MongoDB.
> Let's plan the architecture together before writing any code."

Claude suggested options. I chose Flask + Next.js to combine
Python (which I know) with Next.js (which I wanted to learn).

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
> when the unplayed count drops below 50% of the max."

I came up with the prefetching concept. Claude helped implement
the `is_refilling` flag to prevent duplicate API calls, the `played` field
in MongoDB to track shown countries, and the bulk generation prompt.

**Gemini bulk generation:**
> "I don't want to call Gemini once per country - I want to request
> 15 countries in a single prompt."

I identified the inefficiency. Claude updated the prompt to return
a JSON array of countries in one call.

---

## What AI Generated
- `backend/app.py` - Flask server setup
- `backend/routes/game.py` - API endpoints and refill logic
- `backend/services/database.py` - MongoDB connection and queries
- `backend/services/gemini.py` - Gemini bulk generation
- `backend/seed.py` - database seeding script
- `frontend/app/page.tsx` - Game UI

---

## What I Modified Myself
- Fixed MongoDB SSL certificate error on Mac (`tlsCAFile=certifi.where()`)
- Upgraded Python from 3.8 to 3.11 to support google-genai SDK
- Switched Gemini integration from HTTP requests to google-genai SDK
- Debugged and tested each endpoint manually in the browser
- Fixed git repository conflicts during initial setup
- Identified prefetching concept and bulk generation optimization
- Made all key architectural decisions throughout the process
- Decided to track played countries with a `played` field in MongoDB

---

## AI Configuration
See `.claude.md` in the repository root.

I created this file to set consistent rules for Claude across the project:
- No Hebrew in code
- Minimum changes when necessary
- Explain before writing
- Work one file at a time
- Never rewrite working code

This saved time because I didn't need to repeat the same instructions
in every conversation.