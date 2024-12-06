import streamlit as st
from PIL import Image
import time

# Set page configuration
st.set_page_config(
    page_title="My Cute Baby 💖",
    page_icon="💖",
    layout="wide",
)

# Background music
def play_music():
    audio_file = open("song.mp3", "rb")  # Replace with the path to your music file
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

# Display text messages
def display_text():
    messages = [
        "❤️❤️❤️ My Thanga Mayiluuuuu ❤️❤️❤️",
        "My Sweet Heart ❤️❤️❤️",
        "❤️❤️ My Lovely ThangaPulla ❤️❤️",
        "You are mine PAPA",
        "I love you PAPUDU ❤️ ...",
        "U are the most liked Person ❤️ in my life PAPA...",
        "I will never forget our memories...",
        "Your smile is my favorite thing in the world.",
        "The way you understand and support me means more than words can express.",
        "I am missing 🙁🙁 you every moment PAPA",
        "I Love you PAPA ❤️...You are MINE...",
    ]
    for message in messages:
        st.markdown(f"<h3 style='color:deeppink; text-align:center;'>{message}</h3>", unsafe_allow_html=True)
        time.sleep(2)

# Display GIF or Image
def display_image():
    st.image("image.gif", use_column_width=True)  # Replace with the path to your GIF

# Streamlit Layout
st.title("💖 My Cute Baby 💖")
st.markdown("<h4 style='text-align: center;'>A heartfelt expression of love 💕</h4>", unsafe_allow_html=True)

# Play music in the background
with st.sidebar:
    st.header("Background Music 🎵")
    play_music()

# Main Content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("heart.gif", use_column_width=True)  # Replace with a heart animation GIF if available
    st.markdown("### **Click Below to Start the Love Story!**")
    if st.button("Start 💝"):
        display_text()
        display_image()

st.markdown("<hr style='border:2px solid pink;'>", unsafe_allow_html=True)
st.markdown(
    "<h5 style='text-align: center; color: #ff3366;'>Made with ❤️ by Sudharshan V</h5>",
    unsafe_allow_html=True,
)
