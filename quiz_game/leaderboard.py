import streamlit as st
from datetime import datetime
import json

class Leaderboard:
    def __init__(self):
        if 'leaderboard' not in st.session_state:
            st.session_state.leaderboard = {}
    
    def update_score(self, player_name: str, points: int, reaction_time: float):
        """Update player score based on points and reaction time"""
        time_bonus = max(0, 1 - (reaction_time / 15))  # 15 seconds max time
        final_points = points * (1 + time_bonus)
        
        if player_name not in st.session_state.leaderboard:
            st.session_state.leaderboard[player_name] = {
                'total_score': 0,
                'questions_answered': 0,
                'average_time': 0
            }
        
        player = st.session_state.leaderboard[player_name]
        player['total_score'] += final_points
        player['questions_answered'] += 1
        player['average_time'] = (
            (player['average_time'] * (player['questions_answered'] - 1) + reaction_time)
            / player['questions_answered']
        )
    
    def get_top_players(self, limit: int = 10) -> list:
        """Get top N players sorted by score"""
        sorted_players = sorted(
            st.session_state.leaderboard.items(),
            key=lambda x: x[1]['total_score'],
            reverse=True
        )
        return sorted_players[:limit]
    
    def display_leaderboard(self):
        """Display the leaderboard in Streamlit"""
        st.markdown("## 🏆 Leaderboard")
        
        top_players = self.get_top_players()
        
        for i, (player, stats) in enumerate(top_players):
            # Different styling for top 3
            if i == 0:
                color = "🥇 #FFD700"  # Gold
            elif i == 1:
                color = "🥈 #C0C0C0"  # Silver
            elif i == 2:
                color = "🥉 #CD7F32"  # Bronze
            else:
                color = "#FFFFFF"  # White
                
            st.markdown(
                f'<div style="color: {color};">'
                f'#{i+1} - {player}: {int(stats["total_score"])} points '
                f'(Avg time: {stats["average_time"]:.1f}s)</div>',
                unsafe_allow_html=True
            )
    
    def qualify_for_stage2(self, player_name: str) -> bool:
        """Check if player qualifies for stage 2 (top 10)"""
        top_players = self.get_top_players()
        return any(player[0] == player_name for player in top_players)

    def save_leaderboard(self, filename: str = "leaderboard_history.json"):
        """Save leaderboard to file"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "leaderboard": st.session_state.leaderboard
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4) 