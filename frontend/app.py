import streamlit as st
import pandas as pd

df = pd.read_csv("data/spotify_tracks_data.csv")
st.set_page_config(page_title = "MoodTunes",page_icon = "🎧",layout = "wide")

st.markdown("""
<style>
.main{background-color : #0E1117;}
h1,h2,h3,h4 {color : #FFFFFF;}
.stButton>button {
background-color : #1DB954;
color : white;
border-radius : 10px;
}
.song-card{
background-color :  #1c1c1c;
padding : 12px;
border-radius : 10px;
margin-bottom : 10px;
}
.block-container {
    max-width: 800px;
    padding-top: 2rem;
    margin: auto;
}
</style>
""",unsafe_allow_html = True)

col1 ,col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<h1 style = 'text-align: center;'>🎧 MoodTunes</h1>",unsafe_allow_html =True)
    st.markdown("<p style = 'text-align: center;'>Find Music that matches your mood",unsafe_allow_html = True)

emoji_map = {
    "Happy" : "😄",
    "Sad" : "😔",
    "Angry" : "😡",
    "Relaxed" : "😌",
    "Stressed" : "😩"
}

col1, col2, col3 = st.columns([1,2,1])
with col2:
    mood = st.select_slider(
        "Select your mood",
        options = ['Happy','Sad','Angry','Relaxed','Stressed']
    )

    st.markdown(f"<h3 style = 'text-align: center;'>Current Mood : {mood} {emoji_map[mood]}</h3>",unsafe_allow_html = True)
    btn = st.button("Get Recommendations 🎶",use_container_width = True)

if mood == "Happy":
    filtered = df[(df['energy']>=0.6) & (df['popularity'] > 50)]
elif mood == "Sad":
    filtered = df[(df['energy'] < 0.3)]
elif mood == "Relaxed":
    filtered = df[(df['energy'] >= 0.2) & (df['energy'] < 0.5)]
elif mood == "Angry":
    filtered = df[(df['energy'] >= 0.8)]
elif mood == "Stressed":
    filtered = df[(df['energy'] > 0.4) & (df['energy'] < 0.7)]


top_songs = filtered.sort_values(by = "popularity",ascending = False).head(50)
if len(top_songs)>= 10:

    recommended = top_songs.sample(10)
else:
    recommended = top_songs

if btn:
    st.markdown("<h2 style = 'text-align:center;'> 🎵 Recommended Songs</h2>",unsafe_allow_html = True)
    for i,row in enumerate(recommended.itertuples(),start = 1):
         st.markdown(f"""
    <div class="song-card">
    <b>{i}.{row.track_name}-{row.artists}</b>
    </div>
    """,unsafe_allow_html = True)

st.divider()
st.caption("Made with 💖 using Streamlit")
