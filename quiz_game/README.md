# Medical Quiz Game 🏥

A real-time multiplayer medical quiz game built with Streamlit. Test your medical knowledge against other players in this fast-paced, two-stage competition!

## Features

- Support for up to 50 concurrent players
- Two-stage quiz system with elimination rounds
- Real-time leaderboard with dynamic scoring
- Timer-based questions with bonus points for quick answers
- Medical-themed UI with animations
- Persistent game history

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the files
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Game

1. Start the Streamlit server:

```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Game Rules

### Stage 1
- 20 multiple-choice questions
- 15 seconds per question
- Points awarded based on correctness and response time
- Top 10 players advance to Stage 2

### Stage 2
- 20 advanced questions
- 20 seconds per question
- Higher points available
- Final ranking determines the winner

## Project Structure

```
quiz_game/
├── main.py                  # Main Streamlit app
├── questions/
│   ├── stage1.json         # Stage 1 questions
│   └── stage2.json         # Stage 2 questions
├── leaderboard.py          # Leaderboard management
├── player_session.py       # Player session handling
├── style.css              # Custom styling
└── requirements.txt       # Python dependencies
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 