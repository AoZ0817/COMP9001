from typing import List
from player import Player
from config import *


class Team:
    """Represents a football team"""

    def __init__(self, team_id: int, name: str, initial_budget: int = INITIAL_BUDGET):
        self.team_id = team_id
        self.name = name
        self.budget = initial_budget
        self.players: List[Player] = []
        self.lineup: List[Player] = []

        # Statistics
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

    def add_player(self, player: Player) -> bool:
        """Add player to squad"""
        if len(self.players) >= SQUAD_SIZE:
            return False

        if self.budget < player.salary:
            return False

        self.players.append(player)
        self.budget -= player.salary * 4  # 4 weeks salary upfront
        return True

    def remove_player(self, player: Player) -> bool:
        """Remove player from squad"""
        if player in self.players:
            self.players.remove(player)
            if player in self.lineup:
                self.lineup.remove(player)
            return True
        return False

    def set_lineup(self, players: List[Player]) -> bool:
        """Set the starting lineup for next match"""
        if len(players) != TEAM_SIZE:
            return False

        if not all(p in self.players for p in players):
            return False

        self.lineup = players
        return True

    def pay_wages(self) -> bool:
        """Pay weekly wages to all players"""
        total_wages = sum(p.salary for p in self.players)

        if self.budget < total_wages:
            return False

        self.budget -= total_wages
        return True

    def add_prize_money(self, amount: int):
        """Add prize money from match/competition"""
        self.budget += amount

    def get_team_strength(self) -> float:
        """Calculate average team strength"""
        if not self.lineup:
            return 0

        total_strength = sum(p.get_performance_rating() for p in self.lineup)
        return total_strength / len(self.lineup)

    def get_available_players(self) -> List[Player]:
        """Get players available for selection (not injured)"""
        return [p for p in self.players if not p.injury_status]

    def update_player_injuries(self):
        """Update all player injuries"""
        for player in self.players:
            player.update_injury()

    def rest_players(self):
        """Rest all players to reduce fatigue"""
        for player in self.players:
            player.rest(REST_RECOVERY)

    def get_stats_summary(self) -> dict:
        """Get team statistics summary"""
        matches_played = self.wins + self.draws + self.losses

        return {
            "name": self.name,
            "matches": matches_played,
            "wins": self.wins,
            "draws": self.draws,
            "losses": self.losses,
            "points": self.points,
            "goals_for": self.goals_for,
            "goals_against": self.goals_against,
            "goal_difference": self.goals_for - self.goals_against,
            "budget": self.budget,
            "squad_size": len(self.players)
        }