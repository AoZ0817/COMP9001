"""
main.py
Main entry point for Football Manager Simulator

Run this file to start the game:
    python main.py
"""

import tkinter as tk
from gui import FootballManagerGUI


def main():
    """
    Main function to launch the Football Manager Simulator
    """
    print("=" * 50)
    print("⚽ Football Manager Simulator")
    print("=" * 50)
    print("Starting application...")
    
    try:
        root = tk.Tk()
        app = FootballManagerGUI(root)
        
        print("Application launched successfully!")
        print("Close the window to exit.")
        
        root.mainloop()
        
        print("\nThank you for playing Football Manager Simulator!")
        
    except Exception as e:
        print(f"\n❌ Error starting application: {str(e)}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
