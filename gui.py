"""
gui.py
Main GUI module for Football Manager Simulator
Handles all user interface and interactions
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
from datetime import datetime

from team import Team
from match import Match
from utils import (
    generate_initial_squad,
    generate_transfer_market,
    calculate_transfer_fee,
    save_game,
    load_game,
    format_currency,
    create_random_player
)


class FootballManagerGUI:
    """
    Main GUI application class for Football Manager Simulator
    """
    
    def __init__(self, root):
        """
        Initialize the GUI application
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("⚽ Football Manager Simulator")
        self.root.geometry("1600x960")
        self.root.resizable(True, True)
        self.root.minsize(1100, 720)

        # Game data
        self.team = None
        self.available_players = generate_transfer_market()
        
        # Create interface
        self.create_widgets()
        
        # Try to load existing save
        self.try_load_game()
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Header
        self.create_header()
        
        # Main content area
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Configure grid
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(2, minsize=160)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, minsize=250)
        
        # Three main panels
        self.create_team_panel()
        self.create_player_panel()
        self.create_action_panel()
        
        # Bottom log
        self.create_log_panel()
    
    def create_header(self):
        """Create top header bar"""
        header = ttk.Frame(self.root, relief='raised', borderwidth=2)
        header.pack(fill='x', padx=10, pady=5)
        
        self.club_label = ttk.Label(
            header,
            text="🏆 No Club Created",
            font=('Arial', 16, 'bold')
        )
        self.club_label.pack(side='left', padx=10, pady=5)
        
        self.info_label = ttk.Label(
            header,
            text="💰 Budget: £0 | 📅 Week 1 | ⭐ Reputation: 0",
            font=('Arial', 12)
        )
        self.info_label.pack(side='right', padx=10, pady=5)
        
        ttk.Button(
            header,
            text="🆕 New Game",
            command=self.new_game
        ).pack(side='right', padx=5)
    
    def create_team_panel(self):
        """Create left panel showing team statistics"""
        team_frame = ttk.LabelFrame(self.main_frame, text="📊 Team Statistics", padding=10)
        team_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        self.stats_text = scrolledtext.ScrolledText(
            team_frame,
            width=30,
            height=15,
            font=('Courier', 10)
        )
        self.stats_text.pack(fill='both', expand=True)
        
        self.record_label = ttk.Label(
            team_frame,
            text="Record: 0W 0D 0L",
            font=('Arial', 11, 'bold')
        )
        self.record_label.pack(pady=5)
    
    def create_player_panel(self):
        """Create center panel showing player squad"""
        player_frame = ttk.LabelFrame(self.main_frame, text="👥 Squad", padding=10)
        player_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        # Player list
        columns = ('Name', 'Pos', 'OVR', 'Age', 'Stamina', 'Morale', 'Form')
        self.player_tree = ttk.Treeview(
            player_frame,
            columns=columns,
            show='headings',
            height=12
        )
        
        col_widths = {
            'Name': 100, 'Pos': 60, 'OVR': 60, 'Age': 60,
            'Stamina': 70, 'Morale': 70, 'Form': 60
        }
        
        for col in columns:
            self.player_tree.heading(col, text=col)
            self.player_tree.column(col, width=col_widths[col])
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(
            player_frame,
            orient='vertical',
            command=self.player_tree.yview
        )
        self.player_tree.configure(yscrollcommand=scrollbar.set)
        
        self.player_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Player action buttons
        btn_frame = ttk.Frame(player_frame)
        btn_frame.pack(fill='x', pady=5)
        
        ttk.Button(
            btn_frame,
            text="🏋️ Train Selected",
            command=self.train_player
        ).pack(side='left', padx=2, fill='x', expand=True)
        
        ttk.Button(
            btn_frame,
            text="😴 Rest Selected",
            command=self.rest_player
        ).pack(side='left', padx=2, fill='x', expand=True)
    
    def create_action_panel(self):
        """Create right panel with action buttons"""
        action_frame = ttk.LabelFrame(self.main_frame, text="⚙️ Actions", padding=10)
        action_frame.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)
        
        # Main action buttons
        ttk.Button(
            action_frame,
            text="⚽ Play Match",
            command=self.play_match
        ).pack(fill='x', pady=5)
        
        ttk.Button(
            action_frame,
            text="📅 Advance Week",
            command=self.advance_week
        ).pack(fill='x', pady=5)
        
        ttk.Button(
            action_frame,
            text="🛒 Transfer Market",
            command=self.open_transfer_market
        ).pack(fill='x', pady=5)
        
        ttk.Separator(action_frame, orient='horizontal').pack(fill='x', pady=10)
        
        ttk.Button(
            action_frame,
            text="💾 Save Game",
            command=self.save_game
        ).pack(fill='x', pady=3)
        
        ttk.Button(
            action_frame,
            text="📂 Load Game",
            command=self.load_game
        ).pack(fill='x', pady=3)
        
        ttk.Separator(action_frame, orient='horizontal').pack(fill='x', pady=10)
        
        # Club badge canvas

        self.badge_canvas = tk.Canvas(action_frame, width=180, height=220, bg='#E6F2FF', highlightthickness=0)
        self.badge_canvas.pack(pady=5)
        self._draw_badge()
    
    def create_log_panel(self):
        """Create bottom log panel"""
        log_frame = ttk.LabelFrame(self.root, text="📝 Game Log", padding=5)
        log_frame.pack(fill='x', padx=10, pady=5)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=8,
            font=('Courier', 11)
        )
        self.log_text.pack(fill='both', expand=True)
        self.log_text.tag_configure("log_spacing", spacing1=2, spacing3=6)
        
        self.log("Welcome to Football Manager Simulator! Click 'New Game' to start.")

    def _draw_badge(self):
        """Draw a club crest with a football and dynamic club name."""
        c = self.badge_canvas
        c.delete('all')

        # 读取俱乐部名字（未创建时给占位）
        club_name = self.team.name if getattr(self, "team", None) else "My Club"
        club_name = club_name.strip() or "My Club"

        W, H = int(c['width']), int(c['height'])

        # ---------- 盾牌外形 ----------
        # 外轮廓（深色边）
        shield_outer = [
            (W * 0.5, H * 0.05),  # 顶点
            (W * 0.90, H * 0.22),
            (W * 0.85, H * 0.65),
            (W * 0.50, H * 0.95),
            (W * 0.15, H * 0.65),
            (W * 0.10, H * 0.22),
        ]
        # 内层（浅色填充）
        shield_inner = [(x, y + 2) for (x, y) in shield_outer]  # 稍微下移防止描边重合

        def poly(points, **kw):
            flat = [v for xy in points for v in xy]
            return c.create_polygon(flat, **kw)

        poly(shield_outer, fill='#1E3A8A', outline='#0B1F4B', width=3, smooth=True)
        poly(shield_inner, fill='#3B82F6', outline='', smooth=True)

        # ---------- 足球图案（居中偏上） ----------
        cx, cy, r = W * 0.50, H * 0.38, min(W, H) * 0.20
        c.create_oval(cx - r, cy - r, cx + r, cy + r, fill='white', outline='black', width=3)

        # 中心五边形
        pent = [
            (cx, cy - r * 0.55),
            (cx + r * 0.43, cy - r * 0.18),
            (cx + r * 0.27, cy + r * 0.50),
            (cx - r * 0.27, cy + r * 0.50),
            (cx - r * 0.43, cy - r * 0.18),
        ]
        poly(pent, fill='black', outline='black')

        # 邻接白色多边形（简单蜂窝效果）
        patches = [
            [(cx, cy - r * 0.55), (cx + r * 0.35, cy - r * 0.55), (cx + r * 0.60, cy - r * 0.10),
             (cx + r * 0.43, cy - r * 0.18)],
            [(cx + r * 0.43, cy - r * 0.18), (cx + r * 0.60, cy - r * 0.10), (cx + r * 0.45, cy + r * 0.55),
             (cx + r * 0.27, cy + r * 0.50)],
            [(cx - r * 0.27, cy + r * 0.50), (cx + r * 0.27, cy + r * 0.50), (cx, cy + r * 0.80),
             (cx - r * 0.00, cy + r * 0.80)],
            [(cx - r * 0.43, cy - r * 0.18), (cx - r * 0.60, cy - r * 0.10), (cx - r * 0.45, cy + r * 0.55),
             (cx - r * 0.27, cy + r * 0.50)],
            [(cx, cy - r * 0.55), (cx - r * 0.35, cy - r * 0.55), (cx - r * 0.60, cy - r * 0.10),
             (cx - r * 0.43, cy - r * 0.18)],
        ]
        for p in patches:
            poly(p, fill='white', outline='black', width=2)

        # ---------- 丝带（放名字） ----------
        band_top = H * 0.62
        c.create_rectangle(W * 0.16, band_top, W * 0.84, band_top + 26, fill='#F8FAFF', outline='#0B1F4B', width=2)
        c.create_arc(W * 0.12, band_top - 4, W * 0.30, band_top + 28, start=90, extent=180, style='pieslice',
                     fill='#F8FAFF', outline='#0B1F4B', width=2)
        c.create_arc(W * 0.70, band_top - 4, W * 0.88, band_top + 28, start=-90, extent=180, style='pieslice',
                     fill='#F8FAFF', outline='#0B1F4B', width=2)

        # ---------- 队名文字（根据长度自适应缩放） ----------
        text_size = self._fit_font_for_badge(club_name, max_size=16, min_size=9, max_width=W * 0.60)
        c.create_text(W * 0.50, band_top + 13, text=club_name.upper(), font=('Helvetica', text_size, 'bold'),
                      fill='#0B1F4B')

    def _fit_font_for_badge(self, text, max_size=16, min_size=9, max_width=110):
        """Return a font size that makes 'text' fit within max_width on the badge."""

        # 简单按字符数估算宽度（Tk不直接量字符串宽度，这里用经验系数）
        # 你也可以改成用 tkinter.font.Font 测量精确宽度
        def width_estimate(size):
            # 粗略估计：英文大写约等宽，每个字符 ~0.6*size 像素
            return len(text) * (0.60 * size)

        size = max_size
        while size > min_size and width_estimate(size) > max_width:
            size -= 1
        return max(size, min_size)

    # ==================== Game Logic Methods ====================
    
    def new_game(self):
        """Start a new game"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Create New Club")
        dialog.geometry("400x200")
        dialog.transient(self.root)
        dialog.grab_set()
        
        ttk.Label(
            dialog,
            text="Enter your club name:",
            font=('Arial', 12)
        ).pack(pady=20)
        
        name_entry = ttk.Entry(dialog, font=('Arial', 12), width=30)
        name_entry.pack(pady=10)
        name_entry.insert(0, "My Football Club")
        
        def create():
            name = name_entry.get().strip()
            if name:
                self.team = Team(name, budget=50000000)  # £50 million
                
                # Generate squad
                for player in generate_initial_squad():
                    self.team.add_player(player)
                
                self.update_display()
                self.log(f"✅ Created club: {name}! Starting budget: {format_currency(self.team.budget)}")
                dialog.destroy()
            else:
                messagebox.showwarning("Error", "Please enter a club name!")
        
        ttk.Button(dialog, text="Create", command=create).pack(pady=10)
    
    def train_player(self):
        """Train selected player"""
        if not self.team:
            messagebox.showwarning("Warning", "Please create a club first!")
            return
        
        selected = self.player_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a player!")
            return
        
        index = self.player_tree.index(selected[0])
        player = self.team.players[index]
        
        improvement = player.train()
        if improvement > 0:
            self.log(f"🏋️ {player.name} improved by +{improvement} OVR through training!")
        else:
            self.log(f"🏋️ {player.name} trained but didn't improve (low stamina)...")
        
        self.update_display()
    
    def rest_player(self):
        """Rest selected player"""
        if not self.team:
            return
        
        selected = self.player_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a player!")
            return
        
        index = self.player_tree.index(selected[0])
        player = self.team.players[index]
        player.rest()
        
        self.log(f"😴 {player.name} rested and recovered stamina and morale.")
        self.update_display()
    
    def play_match(self):
        """Play a match"""
        if not self.team:
            messagebox.showwarning("Warning", "Please create a club first!")
            return
        
        if len(self.team.players) < 11:
            messagebox.showwarning("Warning", "You need at least 11 players to play a match!")
            return
        
        # Create opponent
        opponent = Team("Opponent FC", 30000000)
        positions = ['GK', 'DEF', 'DEF', 'DEF', 'DEF', 'MID', 'MID', 'MID', 'FWD', 'FWD', 'FWD']
        for pos in positions:
            opponent.add_player(create_random_player(pos, True))
        
        # Simulate match
        match = Match(self.team, opponent)
        result, home_score, away_score = match.simulate()
        
        # Prize money
        if result == "Victory":
            prize = 1000000
            self.team.budget += prize
            self.team.reputation = min(100, self.team.reputation + 2)
            emoji = "🎉"
        elif result == "Draw":
            prize = 300000
            self.team.budget += prize
            emoji = "😐"
        else:
            prize = 0
            self.team.reputation = max(1, self.team.reputation - 1)
            emoji = "😢"
        
        self.log(f"{emoji} Match {result}! {self.team.name} {home_score} - {away_score} {opponent.name}")
        if prize > 0:
            self.log(f"💰 Prize money: {format_currency(prize)}")
        
        self.update_display()
        
        messagebox.showinfo(
            "Match Result",
            f"{result}!\n\n{self.team.name} {home_score} - {away_score} {opponent.name}\n\nPrize: {format_currency(prize)}"
        )
    
    def advance_week(self):
        """Advance to next week"""
        if not self.team:
            messagebox.showwarning("Warning", "Please create a club first!")
            return
        
        self.team.week += 1
        
        # Pay salaries
        success, total = self.team.pay_salaries()
        if success:
            self.log(f"💸 Week {self.team.week}: Paid salaries {format_currency(total)}")
        else:
            self.log(f"⚠️ Insufficient budget! Need {format_currency(total)}, have {format_currency(self.team.budget)}")
            messagebox.showwarning("Game Over", "Insufficient budget to pay salaries! Game Over!")
            return
        
        # Recover players
        import random
        for player in self.team.players:
            player.stamina = min(100, player.stamina + 10)
            player.form = max(50, min(95, player.form + random.randint(-5, 5)))
        
        self.update_display()
    
    def open_transfer_market(self):
        """Open transfer market window"""
        if not self.team:
            messagebox.showwarning("Warning", "Please create a club first!")
            return
        
        market_window = tk.Toplevel(self.root)
        market_window.title("🛒 Transfer Market")
        market_window.geometry("700x500")
        market_window.transient(self.root)
        
        ttk.Label(
            market_window,
            text=f"Current Budget: {format_currency(self.team.budget)}",
            font=('Arial', 14, 'bold')
        ).pack(pady=10)
        
        # Player list
        columns = ('Name', 'Pos', 'OVR', 'Age', 'Transfer Fee', 'Salary')
        tree = ttk.Treeview(market_window, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        tree.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Fill data
        for player in self.available_players:
            fee = calculate_transfer_fee(player)
            tree.insert('', 'end', values=(
                player.name,
                player.position,
                player.overall,
                player.age,
                format_currency(fee),
                format_currency(player.salary)
            ))
        
        def buy_player():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning("Warning", "Please select a player!")
                return
            
            index = tree.index(selected[0])
            player = self.available_players[index]
            fee = calculate_transfer_fee(player)
            
            if self.team.budget < fee:
                messagebox.showwarning(
                    "Insufficient Budget",
                    f"Need {format_currency(fee)}, but you only have {format_currency(self.team.budget)}"
                )
                return
            
            if len(self.team.players) >= 25:
                messagebox.showwarning("Squad Full", "Your squad already has 25 players!")
                return
            
            self.team.budget -= fee
            self.team.add_player(player)
            self.available_players.remove(player)
            
            self.log(f"✅ Signed {player.name} for {format_currency(fee)}")
            self.update_display()
            tree.delete(selected[0])
            messagebox.showinfo("Success", f"Successfully signed {player.name}!")
        
        ttk.Button(
            market_window,
            text="💰 Buy Selected Player",
            command=buy_player
        ).pack(pady=10)
    
    def save_game(self):
        """Save current game"""
        if not self.team:
            messagebox.showwarning("Warning", "No game to save!")
            return
        
        if save_game(self.team, self.available_players):
            self.log("💾 Game saved successfully!")
            messagebox.showinfo("Success", "Game saved!")
        else:
            messagebox.showerror("Error", "Failed to save game!")
    
    def load_game(self):
        """Load saved game"""
        team, players, timestamp = load_game()
        
        if team is None:
            messagebox.showinfo("Info", "No saved game found!")
            return
        
        self.team = team
        self.available_players = players
        
        self.log(f"📂 Game loaded successfully! Last saved: {timestamp}")
        self.update_display()
        messagebox.showinfo("Success", "Game loaded!")
    
    def try_load_game(self):
        """Try to load game on startup"""
        if os.path.exists('football_manager_save.json'):
            response = messagebox.askyesno(
                "Save Found",
                "Found a saved game. Continue from save?"
            )
            if response:
                self.load_game()
    
    # ==================== Display Updates ====================
    
    def update_display(self):
        """Update all displays"""
        if not self.team:
            return
        
        # Update header
        self.club_label.config(text=f"🏆 {self.team.name}")
        self.info_label.config(
            text=f"💰 Budget: {format_currency(self.team.budget)} | 📅 Week {self.team.week} | ⭐ Reputation: {self.team.reputation}"
        )
        
        # Update record
        self.record_label.config(
            text=f"Record: {self.team.wins}W {self.team.draws}D {self.team.losses}L"
        )
        
        # Update team stats
        self.stats_text.delete('1.0', tk.END)
        stats = f"""
╔══════════════════════════════╗
║   Detailed Team Statistics   ║
╚══════════════════════════════╝

📊 Overview:
   - Squad Size: {len(self.team.players)}/25
   - Team Strength: {self.team.get_team_strength():.1f}
   - Matches Played: {self.team.get_total_matches()}
   - Win Rate: {self.team.get_win_rate():.1f}%

💪 Top 5 Players:
"""
        self.stats_text.insert('1.0', stats)
        
        # Top players
        top_players = sorted(self.team.players, key=lambda p: p.overall, reverse=True)[:5]
        for i, player in enumerate(top_players, 1):
            self.stats_text.insert(tk.END, f"   {i}. {player.name} ({player.position}) - {player.overall}\n")
        
        # Top scorers
        self.stats_text.insert(tk.END, f"\n⚽ Top Scorers:\n")
        top_scorers = sorted(self.team.players, key=lambda p: p.goals, reverse=True)[:3]
        for i, player in enumerate(top_scorers, 1):
            if player.goals > 0:
                self.stats_text.insert(tk.END, f"   {i}. {player.name} - {player.goals} goals\n")
        
        # Top assisters
        self.stats_text.insert(tk.END, f"\n🎯 Top Assists:\n")
        top_assists = sorted(self.team.players, key=lambda p: p.assists, reverse=True)[:3]
        for i, player in enumerate(top_assists, 1):
            if player.assists > 0:
                self.stats_text.insert(tk.END, f"   {i}. {player.name} - {player.assists} assists\n")
        
        # Update player list
        self.player_tree.delete(*self.player_tree.get_children())
        for player in self.team.players:
            self.player_tree.insert('', 'end', values=(
                player.name,
                player.position,
                player.overall,
                player.age,
                f"{player.stamina}%",
                f"{player.morale}%",
                player.form
            ))
    
    def log(self, message):
        """Add message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert('1.0', f"[{timestamp}] {message}\n", "log_spacing")
        self.log_text.see('1.0')


def main():
    """Main entry point"""
    try:
        root = tk.Tk()
        app = FootballManagerGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Program error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
