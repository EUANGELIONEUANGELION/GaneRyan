import streamlit as st
from datetime import datetime
import json

class PlayerSession:
    def __init__(self):
        if 'active_players' not in st.session_state:
            st.session_state.active_players = {}
            
    def add_player(self, player_name: str) -> bool:
        """Add a new player to the session"""
        if len(st.session_state.active_players) >= 50:
            return False
            
        if player_name in st.session_state.active_players:
            return False
            
        st.session_state.active_players[player_name] = {
            'join_time': datetime.now().isoformat(),
            'current_stage': 1,
            'current_question': 0,
            'score': 0,
            'answers': [],
            'is_active': True
        }
        return True
        
    def update_player_progress(self, player_name: str, question_number: int, 
                             answer: int, time_taken: float, is_correct: bool):
        """Update player's progress after answering a question"""
        if player_name in st.session_state.active_players:
            player = st.session_state.active_players[player_name]
            player['current_question'] = question_number
            player['answers'].append({
                'question': question_number,
                'answer': answer,
                'time': time_taken,
                'correct': is_correct
            })
            
    def advance_to_stage2(self, player_name: str):
        """Advance player to stage 2"""
        if player_name in st.session_state.active_players:
            player = st.session_state.active_players[player_name]
            player['current_stage'] = 2
            player['current_question'] = 0
            player['answers'] = []
            
    def get_player_stats(self, player_name: str) -> dict:
        """Get player statistics"""
        if player_name in st.session_state.active_players:
            player = st.session_state.active_players[player_name]
            correct_answers = sum(1 for answer in player['answers'] if answer['correct'])
            avg_time = sum(answer['time'] for answer in player['answers']) / len(player['answers']) if player['answers'] else 0
            
            return {
                'stage': player['current_stage'],
                'question': player['current_question'],
                'correct_answers': correct_answers,
                'total_questions': len(player['answers']),
                'average_time': avg_time
            }
        return None
        
    def remove_player(self, player_name: str):
        """Remove player from session"""
        if player_name in st.session_state.active_players:
            del st.session_state.active_players[player_name]
            
    def get_active_players_count(self) -> int:
        """Get number of active players"""
        return len(st.session_state.active_players)
        
    def save_session_state(self, filename: str = "session_history.json"):
        """Save session state to file"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "active_players": st.session_state.active_players
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4) 