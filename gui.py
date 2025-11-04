import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from player import Player
from team import Team
from league import League
from match import Match
from database import GameDatabase
from config import *


class FootballManagerGUI:
    """Main GUI Application for Football Manager"""

    def __init__(self, root):
        self.root = root
        self.root.title(GAME_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLORS["bg"])

        # Game variables
        self.player_team = None
        self.league = None
        self.database = GameDatabase()
        self.current_round = 0

        # Create main notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)

        # Create tabs
        self.create_main_tab()
        self.create_squad_tab()
        self.create_match_tab()
        self.create_standings_tab()
        self.create_stats_tab()

    def create_main_tab(self):
        """Create main/home tab"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="🏠 Home")

        # Title
        title_label = tk.Label(
            frame, text="Football Manager Simulator",
            font=("Arial", 24, "bold"),
            bg=COLORS["bg"], fg=COLORS["accent"]
        )
        title_label.pack(pady=20)

        # Game status frame
        status_frame = ttk.LabelFrame(frame, text="Game Status", padding=10)
        status_frame.pack(fill="x", padx=20, pady=10)

        self.status_text = tk.Text(status_frame, height=6, width=80, bg=COLORS["bg"], fg=COLORS["fg"])
        self.status_text.pack()

        # Button frame
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="🆕 New Game", command=self.new_game).pack(side="left", padx=5)
        ttk.Button(button_frame, text="💾 Save Game", command=self.save_game).pack(side="left", padx=5)
        ttk.Button(button_frame, text="📂 Load Game", command=self.load_game).pack(side="left", padx=5)

        self.update_status()

    def create_squad_tab(self):
        """Create squad management tab"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="👥 Squad")

        # Squad list
        list_frame = ttk.LabelFrame(frame, text="Current Squad", padding=10)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create treeview
        columns = ("Name", "Position", "Age", "Skill", "Stamina", "Salary", "Fatigue", "Injury")
        self.squad_tree = ttk.Treeview(list_frame, columns=columns, height=15)
        self.squad_tree.column("#0", width=0)

        for col in columns:
            self.squad_tree.column(col, anchor="center", width=100)
            self.squad_tree.heading(col, text=col)

        self.squad_tree.pack(fill="both", expand=True)

        # Control buttons
        control_frame = ttk.Frame(frame)
        control_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(control_frame, text="➕ Add Player", command=self.add_player).pack(side="left", padx=5)
        ttk.Button(control_frame, text="❌ Remove Player", command=self.remove_player).pack(side="left", padx=5)
        ttk.Button(control_frame, text="🔄 Rest Squad", command=self.rest_squad).pack(side="left", padx=5)
        ttk.Button(control_frame, text="🔄 Refresh", command=self.refresh_squad_display).pack(side="left", padx=5)

    def create_match_tab(self):
        """Create match simulation tab"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="⚽ Matches")

        # Match selection
        selection_frame = ttk.LabelFrame(frame, text="Select Match", padding=10)
        selection_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(selection_frame, text="Opponent:").pack(side="left", padx=5)
        self.opponent_var = tk.StringVar()
        self.opponent_combo = ttk.Combobox(selection_frame, textvariable=self.opponent_var, state="readonly", width=30)
        self.opponent_combo.pack(side="left", padx=5)

        # Lineup selection
        lineup_frame = ttk.LabelFrame(frame, text="Set Lineup (11 players)", padding=10)
        lineup_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Available players list
        avail_frame = ttk.LabelFrame(lineup_frame, text="Available Players")
        avail_frame.pack(side="left", fill="both", expand=True, padx=5)

        self.available_list = tk.Listbox(avail_frame, height=15, bg=COLORS["bg"], fg=COLORS["fg"])
        self.available_list.pack(fill="both", expand=True)

        # Selected players list
        selected_frame = ttk.LabelFrame(lineup_frame, text="Selected Lineup")
        selected_frame.pack(side="right", fill="both", expand=True, padx=5)

        self.selected_list = tk.Listbox(selected_frame, height=15, bg=COLORS["bg"], fg=COLORS["fg"])
        self.selected_list.pack(fill="both", expand=True)

        # Control buttons
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(button_frame, text="➕ Add to Lineup", command=self.add_to_lineup).pack(side="left", padx=5)
        ttk.Button(button_frame, text="➖ Remove from Lineup", command=self.remove_from_lineup).pack(side="left", padx=5)
        ttk.Button(button_frame, text="▶️ Play Match", command=self.play_match).pack(side="left", padx=5)
        ttk.Button(button_frame, text="🔄 Refresh", command=self.refresh_match_display).pack(side="left", padx=5)

    def create_standings_tab(self):
        """Create league standings tab"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📊 Standings")

        # Standings treeview
        columns = ("Pos", "Team", "P", "W", "D", "L", "GF", "GA", "GD", "Pts")
        self.standings_tree = ttk.Treeview(frame, columns=columns, height=20)
        self.standings_tree.column("#0", width=0)

        for col in columns:
            self.standings_tree.column(col, anchor="center", width=80)
            self.standings_tree.heading(col, text=col)

        self.standings_tree.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Button(frame, text="🔄 Refresh", command=self.refresh_standings_display).pack(pady=10)

    def create_stats_tab(self):
        """Create statistics tab"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📈 Stats")

        # Top scorers
        scorers_frame = ttk.LabelFrame(frame, text="Top Scorers", padding=10)
        scorers_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("Rank", "Player", "Team", "Goals", "Games")
        self.scorers_tree = ttk.Treeview(scorers_frame, columns=columns, height=15)
        self.scorers_tree.column("#0", width=0)

        for col in columns:
            self.scorers_tree.column(col, anchor="center", width=100)
            self.scorers_tree.heading(col, text=col)

        self.scorers_tree.pack(fill="both", expand=True)

        ttk.Button(frame, text="🔄 Refresh", command=self.refresh_stats_display).pack(pady=10)

    def new_game(self):
        """Start a new game"""
        # Create player team
        self.player_team = Team(1, "Your Team", INITIAL_BUDGET)

        # Generate opponent teams
        team_names = [
            "Arsenal", "Liverpool", "Manchester United", "Manchester City",
            "Chelsea", "Tottenham", "Leicester", "West Ham", "Everton", "Brighton"
        ]

        # Create league
        self.league = League("Premier League")
        self.league.add_team(self.player_team)

        for i, name in enumerate(team_names[:9], start=2):
            team = Team(i, name, INITIAL_BUDGET)
            self.league.add_team(team)

        # Generate initial squads
        self._generate_squads()

        # Generate fixtures
        self.league.generate_fixtures()

        messagebox.showinfo("Success", "New game started! Build your squad and compete in the league.")
        self.update_status()
        self.refresh_squad_display()
        self.refresh_match_display()

    def _generate_squads(self):
        """Generate initial squads for all teams"""
        player_id = 1

        for team in self.league.teams:
            # Generate 25 players per team
            for _ in range(SQUAD_SIZE):
                position = random.choice(POSITIONS)
                player = Player(
                    player_id=player_id,
                    name=f"Player_{player_id}",
                    position=position,
                    age=random.randint(18, 35),
                    skill=random.randint(60, 95),
                    stamina=random.randint(70, 100),
                    salary=POSITION_SALARIES[position],
                    market_value=random.randint(500000, 5000000)
                )
                team.players.append(player)
                player_id += 1

    def add_player(self):
        """Add player to squad (transfer market)"""
        if not self.player_team:
            messagebox.showwarning("Warning", "Start a new game first!")
            return

        # Create transfer dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Transfer Market")
        dialog.geometry("400x300")
        dialog.configure(bg=COLORS["bg"])

        ttk.Label(dialog, text="Position:").pack(padx=10, pady=5)
        position_var = tk.StringVar()
        position_combo = ttk.Combobox(dialog, textvariable=position_var, values=POSITIONS, state="readonly")
        position_combo.pack(padx=10, pady=5)

        ttk.Label(dialog, text="Age:").pack(padx=10, pady=5)
        age_var = tk.IntVar(value=25)
        age_spin = ttk.Spinbox(dialog, from_=18, to=35, textvariable=age_var)
        age_spin.pack(padx=10, pady=5)

        ttk.Label(dialog, text="Skill Level (60-95):").pack(padx=10, pady=5)
        skill_var = tk.IntVar(value=75)
        skill_spin = ttk.Spinbox(dialog, from_=60, to=95, textvariable=skill_var)
        skill_spin.pack(padx=10, pady=5)

        def confirm_transfer():
            position = position_var.get()
            if not position:
                messagebox.showwarning("Warning", "Select a position!")
                return

            player = Player(
                player_id=max(p.player_id for team in self.league.teams for p in team.players) + 1,
                name=f"Transfer_Player_{random.randint(1000, 9999)}",
                position=position,
                age=age_var.get(),
                skill=skill_var.get(),
                stamina=random.randint(70, 100),
                salary=POSITION_SALARIES[position],
                market_value=random.randint(500000, 5000000)
            )

            if self.player_team.add_player(player):
                messagebox.showinfo("Success", f"Signed {player.name}!")
                self.refresh_squad_display()
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Insufficient budget or squad full!")

        ttk.Button(dialog, text="Sign Player", command=confirm_transfer).pack(pady=20)

    def remove_player(self):
        """Remove player from squad"""
        if not self.squad_tree.selection():
            messagebox.showwarning("Warning", "Select a player first!")
            return

        item = self.squad_tree.selection(), [object Object],
        player_name = self.squad_tree.item(item)['values'], [object Object],

        # Find and remove player
        for player in self.player_team.players:
            if player.name == player_name:
                self.player_team.remove_player(player)
                messagebox.showinfo("Success", f"Removed {player_name}!")
                self.refresh_squad_display()
                break

    def rest_squad(self):
        """Rest entire squad to recover fatigue"""
        if not self.player_team:
            messagebox.