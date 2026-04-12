
---

# ⚙️ 2. BACKEND → `backend/README.md`

```markdown
# ⚙️ Backend — FastAPI

This folder contains the backend logic of MoodTunes built using FastAPI.

---

## 🚀 Functionality

- Provides API endpoint for song recommendations
- Filters songs based on:
  - Energy
  - Popularity
- Maps songs to moods

---

## 📌 API Endpoint

### GET /recommend/{mood}

Example: /recommend/Happy 


---

## 📊 Logic

- Energy → Mood mapping
- Top 50 songs selected by popularity
- Random 10 songs returned

---

## 🧪 Run Backend

```bash
uvicorn main:app --reload