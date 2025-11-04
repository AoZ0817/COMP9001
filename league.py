from typing import List, Dict
from team import Team
from match import Match
import random


class League:
    """Represents a football league"""

    def __init__(self, name: str = "Premier League"):
        self.name = name
        self.teams: List[Team] = []
        self.matches: List[Match] = []
        self.current_round = 0

    def add_team(self, team: Team) -> bool:
        """Add team to league"""
        if team not in self.teams:
            self.teams.append(team)
            return True
        return False

    def generate_fixtures(self):
        """Generate league fixtures (double round-robin)"""
        self.matches = []

        # Home and away matches
        for _ in range(2):
            for i, home_team in enumerate(self.teams):
                for away_team in self.teams[i + 1:]:
                    self.matches.append(Match(home_team, away_team))

    def get_standings(self) -> List[Dict]:
        """Get league standings sorted by points"""
        standings = []

        for team in self.teams:
            stats = team.get_stats_summary()
            standings.append(stats)

        # Sort by points (descending), then goal difference
        standings.sort(key=lambda x: (x["points"], x["goal_difference"]), reverse=True)

        for i, team_stats in enumerate(standings):
            team_stats["position"] = i + 1

        return standings

    def get_player_standings(self) -> List[Dict]:
        """Get top scorers across league"""
        player_stats = []

        for team in self.teams:
            for player in team.players:
                player_stats.append({
                    "name": player.name,
                    "team": team.name,
                    "position": player.position,
                    "goals": player.goals,
                    "games": player.games_played,
                    "skill": player.skill
                })

        player_stats.sort(key=lambda x: x["goals"], reverse=True)
        return player_stats[:10]  # Top 10 scorers