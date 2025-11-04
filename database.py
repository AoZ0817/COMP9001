import json
import os
from typing import List, Dict
from team import Team
from player import Player


class GameDatabase:
    """Handle game save/load functionality"""

    SAVE_DIR = "saves"

    def __init__(self):
        if not os.path.exists(self.SAVE_DIR):
            os.makedirs(self.SAVE_DIR)

    def save_game(self, filename: str, player_team: Team, league_data: Dict):
        """Save game to JSON file"""
        save_data = {
            "team": self._serialize_team(player_team),
            "league": league_data,
            "timestamp": str(__import__('datetime').datetime.now())
        }

        filepath = os.path.join(self.SAVE_DIR, f"{filename}.json")

        with open(filepath, 'w') as f:
            json.dump(save_data, f, indent=4)

    def load_game(self, filename: str) -> Dict:
        """Load game from JSON file"""
        filepath = os.path.join(self.SAVE_DIR, f"{filename}.json")

        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            return json.load(f)

    def _serialize_team(self, team: Team) -> Dict:
        """Convert team to dictionary"""
        return {
            "team_id": team.team_id,
            "name": team.name,
            "budget": team.budget,
            "wins": team.wins,
            "draws": team.draws,
            "losses": team.losses,
            "goals_for": team.goals_for,
            "goals_against": team.goals_against,
            "points": team.points,
            "players": [self._serialize_player(p) for p in team.players]
        }

    def _serialize_player(self, player: Player) -> Dict:
        """Convert player to dictionary"""
        return {
            "player_id": player.player_id,
            "name": player.name,
            "position": player.position,
            "age": player.age,
            "skill": player.skill,
            "stamina": player.stamina,
            "salary": player.salary,
            "market_value": player.market_value,
            "fatigue": player.fatigue,
            "games_played": player.games_played,
            "goals": player.goals,
            "injury_status": player.injury_status
        }