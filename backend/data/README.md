# 📊 Dataset Information

This folder contains the dataset used in the **MoodTunes** project for generating mood-based song recommendations.

---

## 📁 File

- `spotify_tracks_data.csv` — Main dataset containing song metadata and audio features

---

## 🧾 Key Features

The dataset includes important attributes such as:

- **track_name** → Name of the song  
- **artists** → Artist(s) associated with the track  
- **energy** → Numerical value (0 to 1) representing intensity and activity of the song  
- **popularity** → Popularity score based on user engagement  

---

## 🧠 Role in the Project

This dataset is used by the backend to:

- Classify songs into different moods based on **energy levels**
- Filter and rank songs using **popularity**
- Provide dynamic recommendations based on user-selected mood  

---

## 🎭 Mood Classification Logic

Songs are categorized into moods using energy values:

| Energy Range | Mood |
|-------------|------|
| ≥ 0.8       | Angry |
| 0.6 – 0.79  | Happy |
| 0.4 – 0.59  | Stressed |
| 0.2 – 0.39  | Relaxed |
| < 0.2       | Sad |

---

## ⚙️ Usage Flow

1. Dataset is loaded using Pandas  
2. Energy values are mapped to moods  
3. Songs are filtered based on selected mood  
4. Top songs are ranked by popularity  
5. A subset is returned as recommendations  

---