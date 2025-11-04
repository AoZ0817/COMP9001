# Configuration file for Football Manager Game
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
GAME_TITLE = "Football Manager Simulator"

# Game Constants
INITIAL_BUDGET = 5000000  # £5 million
MATCH_ROUNDS = 38  # Premier League matches
TEAM_SIZE = 11  # Players on field
SQUAD_SIZE = 25  # Total squad size

# Player Positions
POSITIONS = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
POSITION_SALARIES = {
    "Goalkeeper": 40000,
    "Defender": 50000,
    "Midfielder": 60000,
    "Forward": 80000
}

# Colors for GUI
COLORS = {
    "bg": "#1a1a1a",
    "fg": "#ffffff",
    "primary": "#0066cc",
    "success": "#00cc66",
    "danger": "#cc0000",
    "warning": "#ffaa00",
    "accent": "#ffd700"
}

# Match Constants
MIN_GOALS = 0
MAX_GOALS = 5
FATIGUE_INCREASE = 15
REST_RECOVERY = 10