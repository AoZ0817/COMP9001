"""
utils.py
Utility functions for Football Manager Simulator
Helper functions for player generation, file operations, etc.
"""

import random
import json
from datetime import datetime
from player import Player
from team import Team


# Player name pools for generation
FIRST_NAMES = [
    'Jack', 'Harry', 'Charlie', 'Oliver', 'James', 'Thomas',
    'Lucas', 'Mason', 'Ethan', 'Noah', 'Liam', 'William',
    'Alexander', 'Benjamin', 'Henry', 'Sebastian', 'Daniel', 'Michael'
]

LAST_NAMES = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia',
    'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Wilson', 'Moore',
    'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris'
]


def generate_player_name():
    """
    Generate a random player name
    
    Returns:
        str: Full player name
    """
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    return f"{first} {last}"


def create_random_player(position, is_starter=False):
    """
    Create a random player with generated stats
    
    Args:
        position (str): Player position (GK, DEF, MID, FWD)
        is_starter (bool): Whether this is a starting XI player
        
    Returns:
        Player: New randomly generated player
    """
    name = generate_player_name()
    overall = random.randint(70, 85) if is_starter else random.randint(60, 75)
    age = random.randint(18, 32)
    salary = overall * 10000 + random.randint(5000, 20000)
    
    return Player(name, position, overall, age, salary)


def generate_initial_squad():
    """
    Generate a full starting squad for a new team
    
    Returns:
        list: List of 18 Player objects
    """
    squad = []
    positions = ['GK'] * 2 + ['DEF'] * 6 + ['MID'] * 6 + ['FWD'] * 4
    
    for i, position in enumerate(positions):
        is_starter = i < 11  # First 11 are starters
        player = create_random_player(position, is_starter)
        squad.append(player)
    
    return squad


def generate_transfer_market(players_per_position=5):
    """
    Generate transfer market with available players
    
    Args:
        players_per_position (int): Number of players per position
        
    Returns:
        list: List of available players
    """
    market = []
    positions = ['GK', 'DEF', 'MID', 'FWD']
    
    for position in positions:
        for _ in range(players_per_position):
            player = create_random_player(position)
            market.append(player)
    
    return market


def calculate_transfer_fee(player):
    """
    Calculate transfer fee for a player
    
    Args:
        player (Player): The player
        
    Returns:
        int: Transfer fee in pounds
    """
    return player.overall * 500000


def save_game(team, available_players, filename='football_manager_save.json'):
    """
    Save game state to JSON file
    
    Args:
        team (Team): Current team
        available_players (list): List of available players in market
        filename (str): Save file name
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        save_data = {
            'team': team.to_dict(),
            'available_players': [p.to_dict() for p in available_players],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception as e:
        print(f"Save error: {str(e)}")
        return False


def load_game(filename='football_manager_save.json'):
    """
    Load game state from JSON file
    
    Args:
        filename (str): Save file name
        
    Returns:
        tuple: (team, available_players, timestamp) or (None, None, None) if failed
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            save_data = json.load(f)
        
        team = Team.from_dict(save_data['team'])
        available_players = [Player.from_dict(p) for p in save_data['available_players']]
        timestamp = save_data.get('timestamp', 'Unknown')
        
        return team, available_players, timestamp
    except Exception as e:
        print(f"Load error: {str(e)}")
        return None, None, None


def format_currency(amount):
    """
    Format amount as currency with comma separators
    
    Args:
        amount (int): Amount in pounds
        
    Returns:
        str: Formatted currency string
    """
    return f"£{amount:,}"


def get_position_name(position_code):
    """
    Get full position name from code
    
    Args:
        position_code (str): Position code (GK, DEF, MID, FWD)
        
    Returns:
        str: Full position name
    """
    position_names = {
        'GK': 'Goalkeeper',
        'DEF': 'Defender',
        'MID': 'Midfielder',
        'FWD': 'Forward'
    }
    return position_names.get(position_code, position_code)
