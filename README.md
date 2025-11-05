# ⚽ Football Manager Simulator

A comprehensive football club management simulation game built with Python and Tkinter.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Game Instructions](#game-instructions)
- [Gameplay Tutorial](#gameplay-tutorial)
- [File Structure](#file-structure)
- [Advanced Topics Implemented](#advanced-topics-implemented)
- [Screenshots](#screenshots)
- [Credits](#credits)

---

## 🎮 Project Overview

**Football Manager Simulator** is a single-player management game where you take control of a football club. Manage your squad, train players, compete in matches, buy new talent from the transfer market, and build your club's reputation while maintaining financial stability.

### Target Audience
- Football/Soccer enthusiasts
- Strategy game lovers
- Students learning Python programming
- Anyone interested in sports management simulations

### Key Highlights
- **Complete squad management** with 25-player roster limit
- **Dynamic match simulation** based on team strength and player form
- **Transfer market system** with realistic pricing
- **Financial management** including weekly salaries and prize money
- **Player development** through training and rest mechanics
- **Persistent save system** to continue your progress

---

## ✨ Features

### 🏆 Club Management
- Create and name your own football club
- Starting budget of £50,000,000
- Manage club reputation (1-100)
- Track wins, draws, and losses

### 👥 Squad Management
- Manage up to 25 players in your squad
- Four position types: Goalkeeper (GK), Defender (DEF), Midfielder (MID), Forward (FWD)
- View detailed player statistics:
  - Overall rating (60-95)
  - Age
  - Stamina (0-100%)
  - Morale (0-100%)
  - Form (50-95)
  - Goals and assists
  - Matches played

### 🏋️ Player Development
- **Train players** to improve their overall rating
  - Costs 15 stamina per training session
  - Chance to improve by 0-2 points
  - Best results when stamina > 20%
- **Rest players** to recover stamina and morale
  - Restores 30 stamina points
  - Increases morale by 5 points

### ⚽ Match System
- Play matches against AI opponents
- Match outcomes based on:
  - Team strength (average of top 11 players)
  - Player stamina and morale
  - Player form
  - Home advantage (10% boost)
- **Prize Money**:
  - Victory: £1,000,000 + 2 reputation points
  - Draw: £300,000
  - Defeat: £0 - 1 reputation point
- Players consume 25 stamina per match
- Forwards have increased chance to score
- Midfielders have increased chance to assist

### 🛒 Transfer Market
- 20 players available for purchase (5 per position)
- Transfer fee calculation: Player OVR × £500,000
- Example: 85 OVR player costs £42,500,000
- Each player has unique stats and salary requirements
- Squad limit: 25 players maximum

### 💰 Financial Management
- **Income Sources**:
  - Match prize money
  - Initial budget
- **Expenses**:
  - Weekly player salaries
  - Transfer fees
- **Game Over Condition**: Insufficient funds to pay salaries

### 📅 Time Progression
- Week-by-week progression system
- Automatic salary payments each week
- Players gradually recover stamina (+10 per week)
- Player form fluctuates (±5 per week)

### 💾 Save/Load System
- Save game progress to JSON file
- Auto-detect saves on startup
- Load previous games anytime
- Saves include:
  - Complete team data
  - All player statistics
  - Transfer market state
  - Timestamp

---

## 🔧 Installation

### Prerequisites
- **Python 3.6 or higher** installed on your system
- **Tkinter library** (usually comes pre-installed with Python)

### Verifying Installation

**Check Python version:**
```bash
python --version
# or
python3 --version
```

**Check if Tkinter is available:**
```bash
python -m tkinter
# A small window should appear if Tkinter is installed
```

### Installing Tkinter (if needed)

**Windows:**
- Tkinter comes with Python by default
- If missing, reinstall Python and check "tcl/tk and IDLE" during installation

**macOS:**
```bash
brew install python-tk
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

---

## 🚀 How to Run

### Step 1: Download Files
Download all the following files and place them in the same directory:
- `main.py`
- `gui.py`
- `player.py`
- `team.py`
- `match.py`
- `utils.py`

### Step 2: Navigate to Directory
```bash
cd path/to/football-manager-simulator
```

### Step 3: Run the Game
```bash
python main.py
```
or
```bash
python3 main.py
```

### Alternative: Direct GUI Launch
```bash
python gui.py
```

### Expected Output
```
==================================================
⚽ Football Manager Simulator
==================================================
Starting application...
Application launched successfully!
Close the window to exit.
```

---

## 📖 Game Instructions

### Starting a New Game

1. **Launch the application**
2. **Click "🆕 New Game" button** in the top-right corner
3. **Enter your club name** (e.g., "Manchester United", "Dream FC")
4. **Click "Create"**
5. Your club will be created with:
   - £50,000,000 starting budget
   - 18 initial players (11 starters + 7 reserves)
   - Week 1
   - 50 reputation points

### Understanding the Interface

#### Top Header Bar
- **Left**: Club name with trophy icon 🏆
- **Right**: Current budget 💰, week number 📅, and reputation ⭐

#### Left Panel: Team Statistics 📊
- Squad size (current/maximum)
- Team strength (average rating)
- Match statistics (total matches, win rate)
- **Top 5 Players**: Highest rated players
- **Top Scorers**: Players with most goals ⚽
- **Top Assists**: Players with most assists 🎯
- **Record**: Wins-Draws-Losses

#### Center Panel: Squad List 👥
Displays all players in your squad with columns:
- **Name**: Player's full name
- **Pos**: Position (GK/DEF/MID/FWD)
- **OVR**: Overall rating (ability level)
- **Age**: Player's age
- **Stamina**: Energy level percentage
- **Morale**: Happiness level percentage
- **Form**: Current performance level

#### Right Panel: Action Buttons ⚙️
- **⚽ Play Match**: Simulate a match
- **📅 Advance Week**: Move to next week (pays salaries)
- **🛒 Transfer Market**: Buy new players
- **💾 Save Game**: Save current progress
- **📂 Load Game**: Load saved game
- **Club Badge**: Visual representation (football icon)

#### Bottom Panel: Game Log 📝
- Timestamped log of all events
- Shows match results, training outcomes, transfers, etc.
- Most recent events at the top

---

## 🎓 Gameplay Tutorial

### Week 1: Getting Started

#### Step 1: Review Your Squad
1. Look at the **Squad List** (center panel)
2. Note which players have high OVR (70-85 for starters)
3. Check stamina levels (should be 100% initially)

#### Step 2: Your First Match
1. **Click "⚽ Play Match"**
2. Watch the match result pop-up:
   - Shows final score
   - Indicates Victory/Draw/Defeat
   - Displays prize money earned
3. Check the **Game Log** for details
4. Notice:
   - Budget increased (if you won/drew)
   - Players' stamina decreased
   - Match statistics updated

**Example Log:**
```
[14:25:30] 🎉 Match Victory! Dream FC 3 - 1 Opponent FC
[14:25:31] 💰 Prize money: £1,000,000
```

#### Step 3: Manage Player Stamina
After the match, players will have reduced stamina.

**Option A: Rest Players**
1. Select a player with low stamina (click on them in the list)
2. Click "😴 Rest Selected"
3. Player recovers 30 stamina and 5 morale

**Option B: Train Players**
1. Select a player with good stamina (>50%)
2. Click "🏋️ Train Selected"
3. May improve overall rating by 1-2 points
4. Costs 15 stamina

**Strategy Tip**: Rest key players after matches, train reserves!

### Week 2-4: Building Your Team

#### Financial Management
- **Current Budget**: Check top-right corner
- **Weekly Costs**: Sum of all player salaries
- **Income**: Match prize money

**Example Budget Calculation:**
```
Starting: £50,000,000
Match Win: +£1,000,000
Week 2 Salaries: -£2,500,000
Current: £48,500,000
```

#### Advancing Weeks
1. **Click "📅 Advance Week"**
2. Salaries are automatically deducted
3. If budget < total salaries = **GAME OVER**
4. Players automatically recover:
   - +10 stamina
   - Form changes randomly (±5)

**Game Log Example:**
```
[14:30:15] 💸 Week 2: Paid salaries £2,450,000
```

#### Transfer Market Strategy
When you have £10-20 million saved:

1. **Click "🛒 Transfer Market"**
2. Review available players:
   - 5 Goalkeepers
   - 5 Defenders
   - 5 Midfielders
   - 5 Forwards
3. **Look for**:
   - High OVR (75-85)
   - Young age (18-25 for development)
   - Reasonable salary
4. **Calculate costs**:
   - Transfer fee = OVR × £500,000
   - Plus ongoing weekly salary
5. **Select and click "💰 Buy Selected Player"**

**Example Purchase:**
```
Player: Harry Smith
Position: FWD
OVR: 80
Age: 23
Transfer Fee: £40,000,000
Weekly Salary: £850,000
```

### Week 5-10: Mid-Season Management

#### Training Strategy
**Best Practices:**
- Train young players (18-25) - better improvement chance
- Train players with OVR < 80
- Ensure stamina > 20% before training
- Don't train players needed for next match

**Training Outcomes:**
- 30% chance: +2 OVR
- 40% chance: +1 OVR  
- 30% chance: +0 OVR

#### Match Preparation
**Pre-Match Checklist:**
- Top 11 players have stamina > 50%
- Key forwards well-rested
- No players with morale < 50%

**Post-Match:**
- Rest starters who played
- Check for injuries (low stamina)
- Review goal scorers and assists

#### Squad Rotation
**Why Rotate?**
- Prevent stamina depletion
- Develop younger players
- Maintain morale across squad

**How to Rotate:**
1. Rest Match 1 starters
2. Use reserves for Match 2
3. First team recovers while reserves play

### Week 10+: Long-Term Strategy

#### Building a Dynasty
1. **Financial Stability**
   - Maintain budget > £20 million
   - Balance high/low salary players
   - Win matches consistently for income

2. **Youth Development**
   - Buy young talents (age 18-22)
   - Train them over many weeks
   - Sell older players (30+) if needed

3. **Reputation Growth**
   - Win matches: +2 reputation per win
   - Lose matches: -1 reputation per loss
   - High reputation unlocks better players (future feature)

4. **Records to Beat**
   - 10+ consecutive wins
   - 50+ total wins
   - 90+ win rate percentage
   - All players > 85 OVR

### Advanced Tips

#### Optimal Squad Composition
- **Goalkeepers**: 2 (1 starter, 1 backup)
- **Defenders**: 6-8 (rotate frequently)
- **Midfielders**: 6-8 (high assists potential)
- **Forwards**: 4-5 (goal scorers)

#### Financial Planning
```
Safe Budget Formula:
Minimum Budget = (Weekly Salaries × 4) + £10,000,000

Example:
Weekly Salaries: £2,500,000
Minimum Safe Budget: £20,000,000
```

#### Player Value Assessment
**Good Value Players:**
- OVR 75-80: £37.5M - £40M
- Age 20-25
- Salary < £800,000/week

**Premium Players:**
- OVR 85+: £42.5M+
- Worth it if budget allows
- High salary but high performance

### Saving Your Progress

**When to Save:**
- After major purchases
- After winning streaks
- Before risky decisions
- End of gaming session

**How to Save:**
1. Click "💾 Save Game"
2. Confirmation message appears
3. File saved as `football_manager_save.json`

**Loading Saves:**
- On startup: Auto-prompt if save exists
- Anytime: Click "📂 Load Game"
- Restores all progress exactly as saved

---

## 📁 File Structure

```
football-manager-simulator/
│
├── main.py                          # Main entry point
├── gui.py                           # GUI interface (main application)
├── player.py                        # Player class and methods
├── team.py                          # Team class and methods
├── match.py                         # Match simulation logic
├── utils.py                         # Utility functions (save/load, generation)
│
├── football_manager_save.json       # Save file (created after first save)
│
└── README.md                        # This file
```

### Module Descriptions

#### `main.py`
- Application entry point
- Launches the GUI
- Handles top-level error catching

#### `gui.py` (Main GUI Module)
- Creates and manages all UI elements
- Handles user interactions
- Updates displays
- Coordinates between different modules
- **Lines of Code**: ~550

#### `player.py` (Player Module)
- `Player` class definition
- Player attributes (name, position, stats)
- Training and rest methods
- Match participation
- Serialization (to_dict, from_dict)
- **Lines of Code**: ~150

#### `team.py` (Team Module)
- `Team` class definition
- Squad management (add/remove players)
- Financial tracking (budget, salaries)
- Match statistics (wins, draws, losses)
- Team strength calculation
- **Lines of Code**: ~170

#### `match.py` (Match Simulation Module)
- `Match` class definition
- Match simulation logic
- Score generation based on team strength
- Result determination
- Player stamina updates
- **Lines of Code**: ~100

#### `utils.py` (Utility Module)
- Player name generation
- Random player creation
- Initial squad generation
- Transfer market generation
- Save/load game functions
- Currency formatting
- **Lines of Code**: ~200

**Total Lines of Code**: ~1,170 (excluding comments and blank lines)

---

## 🎯 Advanced Topics Implemented

This project demonstrates mastery of advanced programming concepts required for COMP9001:

### 1. Object-Oriented Programming (OOP) ✅
**Implementation:**
- **Three main classes**: `Player`, `Team`, `Match`
- **Encapsulation**: Data and methods grouped logically
- **Class methods and static methods**: `from_dict()`, `to_dict()`
- **Inheritance potential**: Base class structure for future expansion

**Example:**
```python
class Player:
    def __init__(self, name, position, overall, age, salary):
        self.name = name
        self.overall = overall
        # ... more attributes
    
    def train(self):
        # Method to improve player
        pass
    
    @staticmethod
    def from_dict(data):
        # Factory method to create player from data
        return Player(...)
```

### 2. File I/O Operations ✅
**Implementation:**
- **JSON file format**: Human-readable save files
- **Save function**: Writes complete game state
- **Load function**: Restores game state
- **Error handling**: Try-except blocks for file operations
- **Encoding**: UTF-8 for international character support

**Example:**
```python
def save_game(team, available_players, filename='football_manager_save.json'):
    try:
        save_data = {
            'team': team.to_dict(),
            'available_players': [p.to_dict() for p in available_players],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Save error: {str(e)}")
        return False
```

### 3. GUI Programming with Tkinter ✅
**Implementation:**
- **Multiple frames**: Organized layout with panels
- **Widgets used**:
  - `Treeview`: For player lists
  - `ScrolledText`: For logs and stats
  - `Canvas`: For club badge drawing
  - `Buttons`, `Labels`, `Frames`, `LabelFrames`
- **Event handling**: Button clicks, selections
- **Dialog windows**: Toplevel windows for sub-interfaces
- **Grid and Pack layouts**: Professional arrangement

**Example:**
```python
def create_player_panel(self):
    player_frame = ttk.LabelFrame(self.main_frame, text="👥 Squad")
    player_frame.grid(row=0, column=1, sticky='nsew')
    
    columns = ('Name', 'Pos', 'OVR', 'Age', 'Stamina', 'Morale', 'Form')
    self.player_tree = ttk.Treeview(player_frame, columns=columns)
    # ... configure treeview
```

### 4. Exception Handling ✅
**Implementation:**
- **Try-except blocks**: Around file operations, game logic
- **User-friendly error messages**: MessageBox displays
- **Graceful degradation**: App continues running after errors
- **Logging**: Error details printed for debugging

**Example:**
```python
try:
    with open('football_manager_save.json', 'r', encoding='utf-8') as f:
        save_data = json.load(f)
    return Team.from_dict(save_data['team']), ...
except FileNotFoundError:
    messagebox.showinfo("Info", "No saved game found!")
    return None, None, None
except Exception as e:
    messagebox.showerror("Error", f"Load failed: {str(e)}")
    return None, None, None
```

### Additional Advanced Concepts

#### 5. List Comprehensions and Lambda Functions
```python
# List comprehension for serialization
'players': [p.to_dict() for p in self.players]

# Lambda for sorting
top_players = sorted(self.players, key=lambda p: p.overall, reverse=True)
```

#### 6. Random Number Generation (Simulation)
```python
import random

def _generate_goals(self, attack_strength):
    goals = 0
    for _ in range(random.randint(3, 8)):
        if random.random() < attack_strength * 0.15:
            goals += 1
    return min(goals, 6)
```

#### 7. Date and Time Handling
```python
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Used in save files and game logs
```

---

## 📸 Screenshots

### Main Interface
```
┌─────────────────────────────────────────────────────────────┐
│ 🏆 Dream FC          💰 Budget: £48,500,000 | 📅 Week 3 | ⭐ 54 │
│                                              [🆕 New Game]    │
├────────────┬─────────────────────────────┬──────────────────┤
│ 📊 Team    │ 👥 Squad                    │ ⚙️ Actions        │
│ Statistics │                             │                  │
│            │ Name        Pos OVR Age Stam│ [⚽ Play Match]  │
│ Squad: 18  │ Jack Smith  FWD 82  25  75% │ [📅 Advance Week]│
│ Strength:  │ Harry Brown DEF 78  28  100%│ [🛒 Transfer]    │
│ 76.5       │ ...                         │ [💾 Save]        │
│            │                             │ [📂 Load]        │
│ Top 5:     │ [🏋️ Train] [😴 Rest]       │                  │
│ 1. Smith 82│                             │    [⚽ BADGE]    │
└────────────┴─────────────────────────────┴──────────────────┘
│ 📝 Game Log                                                  │
│ [14:30:15] 🎉 Match Victory! Dream FC 3 - 1 Opponent FC     │
│ [14:30:16] 💰 Prize money: £1,000,000                       │
└──────────────────────────────────────────────────────────────┘
```

---

## 🎓 Learning Outcomes

By studying and running this project, you will learn:

1. **Object-Oriented Design**
   - How to structure classes for a game
   - Separation of concerns (Player, Team, Match)
   - Data encapsulation and methods

2. **GUI Development**
   - Creating professional interfaces with Tkinter
   - Event-driven programming
   - User experience design

3. **Game Logic**
   - Simulation algorithms
   - Balancing mechanics (difficulty, economy)
   - State management

4. **File Persistence**
   - Saving and loading game states
   - JSON data format
   - Data serialization

5. **Software Engineering**
   - Modular code organization
   - Code documentation
   - Error handling
   - Testing and debugging

---

## 🐛 Troubleshooting

### Common Issues

#### "Module not found" Error
```
ModuleNotFoundError: No module named 'tkinter'
```
**Solution**: Install Tkinter (see [Installation](#installation) section)

#### "Permission denied" When Saving
**Solution**: 
- Run from a directory where you have write permissions
- Don't run from system folders (C:\Windows, /usr/bin)

#### Game Window Too Small/Large
**Solution**: 
- Window size is fixed at 1000x700 pixels
- Adjust your display scaling in OS settings
- Or modify `self.root.geometry("1000x700")` in `gui.py`

#### Save File Corrupted
**Solution**:
- Delete `football_manager_save.json`
- Start a new game
- Make sure game isn't forcefully closed during save

---

## 🚀 Future Enhancements (Ideas for Extension)

### Potential Features:
- [ ] Multiple opponent teams with different difficulties
- [ ] League/tournament system
- [ ] Player contracts with expiration dates
- [ ] Injury system
- [ ] Team tactics and formations (4-4-2, 4-3-3, etc.)
- [ ] Stadium upgrades
- [ ] Youth academy system
- [ ] Manager reputation affecting transfers
- [ ] Achievements and trophies
- [ ] Multiplayer (compete with friends)
- [ ] Statistics graphs and charts
- [ ] Player transfer negotiations
- [ ] Staff hiring (coaches, scouts)

---

## 📄 License

This project is created for educational purposes as part of COMP9001 coursework.

**Usage Rights:**
- ✅ Use for learning Python programming
- ✅ Modify and extend for personal projects
- ✅ Reference for understanding game development
- ❌ Do not submit as your own original work without modification
- ❌ Do not use for commercial purposes

---

## 👨‍💻 Credits

**Developer**: [Your Name]  
**Course**: COMP9001 - Python Programming  
**Institution**: [Your University]  
**Year**: 2024

**Technologies Used:**
- Python 3.x
- Tkinter (GUI)
- JSON (Data storage)
- Random (Simulation)

**Inspiration:**
- Football Manager series by Sports Interactive
- FIFA Career Mode by EA Sports

---

## 📞 Support

### Getting Help

**For Technical Issues:**
1. Check the [Troubleshooting](#troubleshooting) section
2. Verify Python and Tkinter installation
3. Read error messages carefully
4. Check file permissions

**For Gameplay Questions:**
1. Read the [Gameplay Tutorial](#gameplay-tutorial) section
2. Review [Game Instructions](#game-instructions)
3. Experiment with different strategies

**Contact:**
- Email: [your.email@university.edu]
- Tutorial: [Your tutorial day/time]
- Tutor: [Your tutor's name]

---

## 🎉 Acknowledgments

Thank you to:
- COMP9001 teaching staff for project guidelines
- Python community for documentation
- Tkinter developers for the GUI framework
- All football management game developers for inspiration

---

**Enjoy managing your football club! ⚽🏆**

*Last Updated: November 2024*
*Version: 1.0*
