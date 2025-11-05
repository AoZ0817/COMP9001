"""
player.py
Player class module for Football Manager Simulator
Handles all player-related attributes and behaviors
"""

import random


class Player:
    """
    Player class representing a football player
    
    Attributes:
        name (str): Player's full name
        position (str): Player's position (GK, DEF, MID, FWD)
        overall (int): Overall rating (1-99)
        age (int): Player's age
        salary (int): Weekly salary in pounds
        stamina (int): Current stamina level (0-100)
        morale (int): Player's morale (0-100)
        form (int): Current form/performance level (50-95)
        goals (int): Total goals scored
        assists (int): Total assists made
        matches_played (int): Total matches played
    """
    
    def __init__(self, name, position, overall, age, salary):
        """
        Initialize a new player
        
        Args:
            name (str): Player's name
            position (str): Playing position
            overall (int): Overall rating
            age (int): Player's age
            salary (int): Weekly salary
        """
        self.name = name
        self.position = position
        self.overall = overall
        self.age = age
        self.salary = salary
        self.stamina = 100
        self.morale = 75
        self.form = random.randint(60, 85)
        self.goals = 0
        self.assists = 0
        self.matches_played = 0
    
    def train(self):
        """
        Train the player to improve abilities
        
        Returns:
            int: Amount of improvement gained (0-2)
        """
        if self.stamina > 20:
            self.stamina -= 15
            improvement = random.randint(0, 2)
            if self.overall < 95 and random.random() > 0.7:
                self.overall += improvement
                return improvement
        return 0
    
    def rest(self):
        """
        Rest the player to recover stamina and morale
        """
        self.stamina = min(100, self.stamina + 30)
        self.morale = min(100, self.morale + 5)
    
    def play_match(self):
        """
        Player participates in a match
        Updates stamina and may score goals or assists
        """
        self.stamina = max(0, self.stamina - 25)
        self.matches_played += 1

    
    def get_match_rating(self):
        """
        Calculate player's match performance rating
        
        Returns:
            float: Performance rating (50-99)
        """
        base = self.overall
        form_bonus = (self.form - 70) * 0.3
        stamina_penalty = (100 - self.stamina) * 0.1
        morale_bonus = (self.morale - 50) * 0.15
        return max(50, min(99, base + form_bonus - stamina_penalty + morale_bonus))
    
    def to_dict(self):
        """
        Convert player object to dictionary for saving
        
        Returns:
            dict: Player data as dictionary
        """
        return {
            'name': self.name,
            'position': self.position,
            'overall': self.overall,
            'age': self.age,
            'salary': self.salary,
            'stamina': self.stamina,
            'morale': self.morale,
            'form': self.form,
            'goals': self.goals,
            'assists': self.assists,
            'matches_played': self.matches_played
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a player from dictionary data
        
        Args:
            data (dict): Player data dictionary
            
        Returns:
            Player: New player object
        """
        player = Player(
            data['name'],
            data['position'],
            data['overall'],
            data['age'],
            data['salary']
        )
        player.stamina = data['stamina']
        player.morale = data['morale']
        player.form = data['form']
        player.goals = data['goals']
        player.assists = data['assists']
        player.matches_played = data['matches_played']
        return player
    
    def __str__(self):
        """String representation of player"""
        return f"{self.name} ({self.position}) - OVR: {self.overall}"
    
    def __repr__(self):
        """Detailed representation of player"""
        return f"Player('{self.name}', '{self.position}', {self.overall})"
