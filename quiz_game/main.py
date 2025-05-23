import streamlit as st
import json
from datetime import datetime
import time
from streamlit_lottie import st_lottie
import requests

# Page config
st.set_page_config(
    page_title="Medical Quiz Game",
    page_icon="🏥",
    layout="wide"
)

# Initialize session state
if 'player_name' not in st.session_state:
    st.session_state.player_name = None
if 'current_stage' not in st.session_state:
    st.session_state.current_stage = 1
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_number' not in st.session_state:
    st.session_state.question_number = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'players' not in st.session_state:
    st.session_state.players = {}

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load medical animation
lottie_medical = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_5njp3vgg.json")

# Main UI
st.title("🏥 Medical Quiz Game")

if st.session_state.player_name is None:
    # Login page
    st.markdown("""
    ## Welcome to the Medical Quiz Challenge!
    Enter your name to join the game. Get ready to test your medical knowledge!
    """)
    
    # Display medical animation
    st_lottie(lottie_medical, height=200)
    
    with st.form("login_form"):
        player_name = st.text_input("Enter your name:")
        submit_button = st.form_submit_button("Join Game")
        
        if submit_button and player_name:
            if len(st.session_state.players) >= 50:
                st.error("Maximum number of players (50) reached!")
            elif player_name in st.session_state.players:
                st.error("This name is already taken!")
            else:
                st.session_state.player_name = player_name
                st.session_state.players[player_name] = {
                    "score": 0,
                    "stage": 1,
                    "join_time": datetime.now().isoformat()
                }
                st.rerun()

else:
    # Game interface for logged-in players
    st.sidebar.markdown(f"**Player:** {st.session_state.player_name}")
    st.sidebar.markdown(f"**Score:** {st.session_state.score}")
    st.sidebar.markdown(f"**Stage:** {st.session_state.current_stage}")
    
    # Placeholder for actual game logic
    st.markdown("### Game in progress...")
    st.markdown("Stay tuned for the quiz questions!") 