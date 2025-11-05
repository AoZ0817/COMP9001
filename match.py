"""
match.py
Match simulation module for Football Manager Simulator
Handles match logic and scoring
"""

import random


class Match:
    """
    Match class for simulating football matches
    
    Attributes:
        home_team (Team): Home team
        away_team (Team): Away team
        home_score (int): Home team's score
        away_score (int): Away team's score
    """
    
    def __init__(self, home_team, away_team):
        """
        Initialize a new match
        
        Args:
            home_team (Team): Home team
            away_team (Team): Away team
        """
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0
    
    def simulate(self):
        """
        Simulate the match and return results
        
        Returns:
            tuple: (result: str, home_score: int, away_score: int)
                result is "Victory", "Draw", or "Defeat" from home team perspective
        """
        # Get team strengths
        home_strength = self.home_team.get_team_strength()
        away_strength = self.away_team.get_team_strength()
        
        # Apply home advantage (10% boost)
        home_strength *= 1.1
        
        # Calculate attack power
        home_attack = home_strength / 10
        away_attack = away_strength / 10
        
        # Generate goals
        self.home_score = self._generate_goals(home_attack)
        self.away_score = self._generate_goals(away_attack)
        
        # Update player states (only for home team - the player's team)
        for player in self.home_team.players[:11]:
            player.play_match()
        
        # Update match statistics
        if self.home_score > self.away_score:
            self.home_team.wins += 1
            result = "Victory"
        elif self.home_score < self.away_score:
            self.home_team.losses += 1
            result = "Defeat"
        else:
            self.home_team.draws += 1
            result = "Draw"
        
        return result, self.home_score, self.away_score
    
    def _generate_goals(self, attack_strength):
        """
        Generate number of goals based on attack strength
        
        Args:
            attack_strength (float): Team's attacking power
            
        Returns:
            int: Number of goals scored
        """
        goals = 0
        # Simulate multiple scoring chances
        for _ in range(random.randint(3, 8)):
            if random.random() < attack_strength * 0.15:
                goals += 1
        return min(goals, 6)  # Cap at 6 goals for realism
    
    def get_match_summary(self):
        """
        Get a formatted match summary
        
        Returns:
            str: Match summary string
        """
        return f"{self.home_team.name} {self.home_score} - {self.away_score} {self.away_team.name}"
    
    def __str__(self):
        """String representation of match"""
        return self.get_match_summary()
