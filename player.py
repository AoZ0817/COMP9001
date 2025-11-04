import random
from dataclasses import dataclass
from typing import Optional


@dataclass
class Player:
    """Represents a football player"""

    player_id: int
    name: str
    position: str
    age: int
    skill: int  # 1-100
    stamina: int  # 1-100
    salary: int
    market_value: int

    def __post_init__(self):
        self.fatigue = 0
        self.games_played = 0
        self.goals = 0
        self.assists = 0
        self.injury_status = False
        self.injury_weeks = 0

    def update_fatigue(self, increase: int):
        """Update player fatigue after match"""
        self.fatigue = min(100, self.fatigue + increase)

    def rest(self, recovery: int):
        """Recover fatigue during rest"""
        self.fatigue = max(0, self.fatigue - recovery)

    def check_injury(self):
        """Random injury check (5% chance per match)"""
        if random.random() < 0.05:
            self.injury_status = True
            self.injury_weeks = random.randint(1, 4)
            return True
        return False

    def update_injury(self):
        """Update injury status"""
        if self.injury_status:
            self.injury_weeks -= 1
            if self.injury_weeks <= 0:
                self.injury_status = False

    def get_performance_rating(self) -> float:
        """Calculate player performance based on skill, stamina, and fatigue"""
        base_performance = (self.skill * 0.7) + (self.stamina * 0.3)
        fatigue_penalty = (self.fatigue / 100) * 30
        injury_penalty = 50 if self.injury_status else 0

        return max(0, base_performance - fatigue_penalty - injury_penalty)

    def __str__(self):
        return f"{self.name} ({self.position}) - Skill: {self.skill}, Age: {self.age}"