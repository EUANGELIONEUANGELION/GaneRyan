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
if 'current_question' not in st.session_state:
    st.session_state.current_question = None

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_questions(stage):
    try:
        with open(f"questions/stage{stage}.json", "r") as f:
            return json.load(f)["questions"]
    except:
        return []

# Load medical animation
lottie_medical = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_5njp3vgg.json")

# Main UI
st.title("🏥 Medical Quiz Game")

if st.session_state.player_name is None:
    # Login page
    st.markdown("""
    ## Welcome to the Medical Quiz Challenge!
    Enter your name to start the game. Get ready to test your medical knowledge!
    """)
    
    # Display medical animation
    st_lottie(lottie_medical, height=200)
    
    with st.form("login_form"):
        player_name = st.text_input("Enter your name:")
        submit_button = st.form_submit_button("Start Game")
        
        if submit_button and player_name:
            st.session_state.player_name = player_name
            st.session_state.start_time = time.time()
            st.rerun()

else:
    # Game interface for logged-in players
    st.sidebar.markdown(f"**Player:** {st.session_state.player_name}")
    st.sidebar.markdown(f"**Score:** {st.session_state.score}")
    st.sidebar.markdown(f"**Stage:** {st.session_state.current_stage}")
    
    # Game has started
    questions = load_questions(st.session_state.current_stage)
    
    if st.session_state.question_number >= len(questions):
        st.success("Congratulations! You've completed this stage!")
        if st.session_state.current_stage == 1:
            st.markdown("Get ready for Stage 2!")
            if st.button("Proceed to Stage 2"):
                st.session_state.current_stage = 2
                st.session_state.question_number = 0
                st.rerun()
        else:
            st.markdown("### 🎉 Congratulations! You've completed the game!")
            st.markdown(f"Final Score: **{st.session_state.score}** points")
            if st.button("Play Again"):
                st.session_state.clear()
                st.rerun()
    else:
        current_question = questions[st.session_state.question_number]
        
        # Display question
        st.markdown(f"### Question {st.session_state.question_number + 1}")
        st.markdown(current_question["question"])
        
        # Display options
        answer = st.radio("Choose your answer:", 
                        options=current_question["options"],
                        key=f"question_{st.session_state.question_number}")
        
        # Submit answer button
        if st.button("Submit Answer"):
            selected_index = current_question["options"].index(answer)
            if selected_index == current_question["correct_answer"]:
                st.success("Correct! 🎉")
                st.session_state.score += current_question["points"]
            else:
                st.error("Incorrect! 😔")
                correct_answer = current_question["options"][current_question["correct_answer"]]
                st.markdown(f"The correct answer was: **{correct_answer}**")
            
            st.session_state.question_number += 1
            time.sleep(1)
            st.rerun() 