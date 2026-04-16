from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv('data/spotify_tracks_data.csv')


def map_mood(energy):
    if energy >= 0.8:
        return "Angry"
    elif energy >= 0.6:
        return "Happy"
    elif energy >= 0.4:
        return "Stressed"
    elif energy >= 0.2:
        return "Relaxed"
    else:
        return "Sad"

df['mood'] = df['energy'].apply(map_mood)


@app.get("/recommend/{mood}")
def recommend(mood: str):

    filtered = df[df['mood'] == mood]

    top_songs = filtered.sort_values(by='popularity', ascending=False).head(50)

    if len(top_songs) == 0:
        return {"songs": []}

    if len(top_songs) >= 10:
        recommended = top_songs.sample(10)
    else:
        recommended = top_songs   

    result = []

    for _, row in recommended.iterrows():
        result.append({
            "Track_name": row["track_name"],
            "Artist": row["artists"]
        })

    return {"songs": result}