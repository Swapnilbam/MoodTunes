import streamlit as st
import requests

st.set_page_config(page_title="MoodTunes", page_icon="🎧", layout="wide")

st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #1a0033, #0a001a);
}

.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 2rem;
}

/* Title */
h1 {
    text-align: center;
    font-size: 42px;
}

/* Song Card */
.song-card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 14px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Hover feel */
.song-card:hover {
    background: linear-gradient(135deg, #7F00FF, #E100FF);
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #7F00FF, #E100FF);
    color: white;
    border-radius: 25px;
    height: 50px;
    font-size: 16px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<h1>🎧 MoodTunes</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Find Music that matches your mood</p>", unsafe_allow_html=True)

emoji_map = {
    "Happy": "😄",
    "Sad": "😔",
    "Angry": "😡",
    "Relaxed": "😌",
    "Stressed": "😩"
}

col1, col2, col3 = st.columns([1,2,1])
with col2:
    mood = st.select_slider(
        "Select your mood",
        options=['Happy','Sad','Angry','Relaxed','Stressed']
    )

    st.markdown(f"""
    <div style="text-align:center; font-size:22px; margin-top:10px; margin-bottom:20px;">
        Current Mood: <b>{mood}</b> {emoji_map[mood]}
    </div>
    """, unsafe_allow_html=True)

    btn = st.button("Get Recommendations 🎶", use_container_width=True)

if btn:
    try:
        response = requests.get(f"http://127.0.0.1:8000/recommend/{mood}")
        data = response.json()

        if len(data["songs"]) == 0:
            st.warning("No songs found for this mood 😔")
        else:
            
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #7F00FF, #E100FF);
                padding: 20px;
                border-radius: 16px;
                text-align: center;
                margin-bottom: 25px;
                color:white;
            ">
                <h2>🎵 Your Mood Playlist</h2>
            </div>
            """, unsafe_allow_html=True)

            
            for i, song in enumerate(data["songs"], start=1):

                search_query = f"{song['Track_name']} {song['Artist']}".replace(" ", "%20")
                youtube_url = f"https://www.youtube.com/results?search_query={search_query}"

                with st.container():
                    col1, col2 = st.columns([8,1])

                    with col1:
                        st.markdown(f"""
                        <div class="song-card">
                            <b>{i}. {song['Track_name']}</b><br>
                            <span style="color:#bbb;">{song['Artist']}</span>
                        </div>
                        """, unsafe_allow_html=True)

                    with col2:
                        st.link_button("▶️", youtube_url)

    except:
        st.error("⚠️ Backend not running or connection failed")


st.markdown("""
<hr style="margin-top:40px; border:0.5px solid #333;">

<div style="text-align:center; color:#aaa; font-size:14px;">
    Made with 💖 using <b>Streamlit</b><br>
    <span style="font-size:13px;">by Swapnil Bam</span>
</div>
""", unsafe_allow_html=True)