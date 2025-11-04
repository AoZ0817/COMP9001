import random
from typing import Tuple
from team import Team
from config import *


class Match:
    """Represents a football match"""

    def __init__(self, home_team: Team, away_team: Team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = 0
        self.away_goals = 0
        self.match_events = []
        self.is_played = False

    def simulate(self) -> Tuple[int, int]:
        """Simulate match and return goals"""
        self.match_events = []

        # Check if teams have valid lineups
        if not self.home_team.lineup or not self.away_team.lineup:
            raise ValueError("Both teams must have valid lineups")

        # Simulate match
        home_strength = self.home_team.get_team_strength()
        away_strength = self.away_team.get_team_strength()

        # Home advantage factor
        home_advantage = home_strength * 1.05

        # Calculate goals based on team strength
        self.home_goals = self._calculate_goals(home_advantage, away_strength)
        self.away_goals = self._calculate_goals(away_strength, home_strength)

        # Update player statistics
        self._update_player_stats()

        # Update team records
        self._update_team_records()

        self.is_played = True
        return self.home_goals, self.away_goals

    def _calculate_goals(self, attacking_strength: float, defending_strength: float) -> int:
        """Calculate goals based on team strengths"""
        strength_ratio = attacking_strength / (defending_strength + 1)
        base_goals = min(MAX_GOALS, max(MIN_GOALS, strength_ratio / 20))

        # Add randomness
        goals = int(base_goals + random.random() * 2)
        return max(MIN_GOALS, min(MAX_GOALS, goals))

    def _update_player_stats(self):
        """Update player statistics after match"""
        # Update fatigue for all players in lineup
        for player in self.home_team.lineup:
            player.update_fatigue(FATIGUE_INCREASE)
            player.games_played += 1
            player.check_injury()

        for player in self.away_team.lineup:
            player.update_fatigue(FATIGUE_INCREASE)
            player.games_played += 1
            player.check_injury()

    def _update_team_records(self):
        """Update team records based on match result"""
        self.home_team.goals_for += self.home_goals
        self.home_team.goals_against += self.away_goals
        self.away_team.goals_for += self.away_goals
        self.away_team.goals_against += self.home_goals

        if self.home_goals > self.away_goals:
            self.home_team.wins += 1
            self.home_team.points += 3
            self.away_team.losses += 1
            self.match_events.append(f"{self.home_team.name} wins {self.home_goals}-{self.away_goals}")
        elif self.home_goals < self.away_goals:
            self.away_team.wins += 1
            self.away_team.points += 3
            self.home_team.losses += 1
            self.match_events.append(f"{self.away_team.name} wins {self.away_goals}-{self.home_goals}")
        else:
            self.home_team.draws += 1
            self.home_team.points += 1
            self.away_team.draws += 1
            self.away_team.points += 1
            self.match_events.append(f"{self.home_team.name} draws {self.home_goals}-{self.away_goals}")

        # Award prize money
        prize_money = 500000
        self.home_team.add_prize_money(prize_money // 2)
        self.away_team.add_prize_money(prize_money // 2)

    def get_result_string(self) -> str:
        """Get match result as string"""
        return f"{self.home_team.name} {self.home_goals} - {self.away_goals} {self.away_team.name}"