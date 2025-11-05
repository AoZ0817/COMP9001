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
        # 计算两队强度（保持你原来的逻辑）
        home_strength = self.home_team.get_team_strength()
        away_strength = self.away_team.get_team_strength()

        # 主场优势
        home_strength *= 1.1

        # 进攻强度
        home_attack = home_strength / 10
        away_attack = away_strength / 10

        # 生成进球数（沿用你原来的“多次机会+概率进球”）
        self.home_score = self._generate_goals(home_attack)
        self.away_score = self._generate_goals(away_attack)

        # 先给主队首发球员结算体能/出场（保持你原本只更新主队的做法）
        for player in self.home_team.players[:11]:
            player.play_match()

        # ✅ 关键：把“实际进球数”分配给具体球员（射手/助攻）
        self._assign_goals_and_assists(self.home_team, self.home_score)

        # （可选）是否也给客队分配个人数据：
        # self._assign_goals_and_assists(self.away_team, self.away_score)

        # 更新比赛结果到战绩
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

    def _choose_player(self, team, pos_weights):
        """Pick a player from starting 11 with weighted probability by position & form."""
        starters = team.players[:11]  # 只在首发里分配
        if not starters:
            return None

        def weight(p):
            base = pos_weights.get(p.position, 1.0)
            form_bonus = max(0.5, (p.form - 50) / 50)  # 50~95 -> 0.5~0.9
            return base * form_bonus

        weights = [weight(p) for p in starters]
        return random.choices(starters, weights=weights, k=1)[0]

    def _assign_goals_and_assists(self, team, goals):
        """
        For each real goal scored by 'team', assign a scorer and (70% chance) an assister.
        FWD最可能进球，其次MID，再次DEF；助攻以MID、FWD为主。
        """
        for _ in range(goals):
            # 射手
            scorer = self._choose_player(team, {'FWD': 5, 'MID': 2, 'DEF': 1, 'GK': 0.2})
            if scorer:
                scorer.goals += 1
            # 助攻（70% 概率有助攻；且不能是同一人）
            if random.random() < 0.7 and len(team.players) >= 2:
                assister = self._choose_player(team, {'MID': 4, 'FWD': 2, 'DEF': 1})
                if assister and assister is not scorer:
                    assister.assists += 1

    def __str__(self):
        """String representation of match"""
        return self.get_match_summary()

