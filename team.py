"""
team.py
Team class module for Football Manager Simulator
Manages team data, squad, and finances
"""

from player import Player


class Team:
    """
    Team class representing a football club
    
    Attributes:
        name (str): Team name
        budget (int): Available budget in pounds
        players (list): List of Player objects
        wins (int): Number of wins
        draws (int): Number of draws
        losses (int): Number of losses
        week (int): Current week number
        reputation (int): Club reputation (1-100)
    """
    
    def __init__(self, name, budget):
        """
        Initialize a new team
        
        Args:
            name (str): Team name
            budget (int): Starting budget
        """
        self.name = name
        self.budget = budget
        self.players = []
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.week = 1
        self.reputation = 50
    
    def add_player(self, player):
        """
        Add a player to the squad
        
        Args:
            player (Player): Player to add
            
        Returns:
            bool: True if successful, False if squad is full
        """
        if len(self.players) < 25:
            self.players.append(player)
            return True
        return False
    
    def remove_player(self, player):
        """
        Remove a player from the squad
        
        Args:
            player (Player): Player to remove
            
        Returns:
            bool: True if successful, False if player not found
        """
        if player in self.players:
            self.players.remove(player)
            return True
        return False
    
    def get_team_strength(self):
        """
        Calculate overall team strength based on top 11 players
        
        Returns:
            float: Average rating of starting 11
        """
        if not self.players:
            return 0
        
        # Get ratings of top 11 players
        top_11 = sorted(self.players, key=lambda p: p.get_match_rating(), reverse=True)[:11]
        total = sum(p.get_match_rating() for p in top_11)
        return total / min(11, len(self.players))
    
    def pay_salaries(self):
        """
        Pay weekly salaries to all players
        
        Returns:
            tuple: (success: bool, total_cost: int)
        """
        total = sum(p.salary for p in self.players)
        if self.budget >= total:
            self.budget -= total
            return True, total
        return False, total
    
    def get_total_matches(self):
        """Get total number of matches played"""
        return self.wins + self.draws + self.losses
    
    def get_win_rate(self):
        """
        Calculate win percentage
        
        Returns:
            float: Win rate as percentage
        """
        total = self.get_total_matches()
        if total == 0:
            return 0.0
        return (self.wins / total) * 100
    
    def to_dict(self):
        """
        Convert team object to dictionary for saving
        
        Returns:
            dict: Team data as dictionary
        """
        return {
            'name': self.name,
            'budget': self.budget,
            'players': [p.to_dict() for p in self.players],
            'wins': self.wins,
            'draws': self.draws,
            'losses': self.losses,
            'week': self.week,
            'reputation': self.reputation
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a team from dictionary data
        
        Args:
            data (dict): Team data dictionary
            
        Returns:
            Team: New team object
        """
        team = Team(data['name'], data['budget'])
        team.players = [Player.from_dict(p) for p in data['players']]
        team.wins = data['wins']
        team.draws = data['draws']
        team.losses = data['losses']
        team.week = data['week']
        team.reputation = data['reputation']
        return team
    
    def __str__(self):
        """String representation of team"""
        return f"{self.name} - W:{self.wins} D:{self.draws} L:{self.losses}"
    
    def __repr__(self):
        """Detailed representation of team"""
        return f"Team('{self.name}', budget=£{self.budget:,})"
