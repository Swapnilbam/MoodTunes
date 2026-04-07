
---

# 📁 `backend/README.md`

```md
# ⚙️ Backend (FastAPI)

This folder contains the backend logic of the application using FastAPI.

## 📌 Responsibilities
- Handle API requests
- Process mood input
- Recommend songs using dataset
- Connect with database (MySQL)

## 📂 Files
- `main.py` → FastAPI entry point
- `recommender.py` → mood → song logic
- `database.py` → database connection
- `models.py` → database models (optional)

## 🚀 Run Backend
```bash
uvicorn main:app --reload
