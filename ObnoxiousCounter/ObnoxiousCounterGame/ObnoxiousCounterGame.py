import sys
import os
import threading
import tkinter as tk
from tkinter import ttk

### A simple idle clicker game with a tiny twist.
### -Mishaela Pedersen 4/13/26

class IdleClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Suspicious Idle Clicker")
        self.root.geometry("300x400")

        # Game State
        self.score = 0.0
        self.cps = 0.0  # Clicks Per Second
        self.upgrade_cost = 10
        self.time_since_click = 0

        # UI Elements
        self.label_big = tk.Label(root,text="Idle Clicker")
        self.label_score = tk.Label(root, text=f"{self.score:.0f}", font=("Arial", 24))
        self.label_score.pack(pady=20)

        self.label_cps = tk.Label(root, text=f"CPS: {self.cps:.0f}", font=("Arial", 12))
        self.label_cps.pack()

        self.click_btn = tk.Button(root, text="Click Me", command=self.manual_click, 
                                   width=20, height=5, bg="lightblue")
        self.click_btn.pack(pady=20)

        self.upgrade_btn = tk.Button(root, text=f"Buy Upgrade ({self.upgrade_cost})", 
                                     command=self.buy_upgrade)
        self.upgrade_btn.pack(pady=10)

        # Start the background idle loop
        self.update_idle()

    # For every time user clicks button
    def manual_click(self):
        self.score += 1
        self.time_since_click = 0
        self.refresh_ui()
    
    # Upgrade button
    def buy_upgrade(self):
        if self.score >= self.upgrade_cost:
            self.score -= self.upgrade_cost
            self.cps += 0.5
            self.upgrade_cost = int(self.upgrade_cost * 1.5)  # Increase price
            self.refresh_ui()
            self.upgrade_btn.config(text=f"Buy Upgrade ({self.upgrade_cost})")

    # Refresh the display to display new numbers
    def refresh_ui(self):
        self.label_score.config(text=f"{self.score:.0f}")
        self.label_cps.config(text=f"CPS: {self.cps}")

    # Passive idle code
    def update_idle(self):
        """Adds passive income and schedules next update."""
        self.time_since_click += 1
        if self.cps > 0.0:
            self.score += self.cps
            self.refresh_ui()
        if self.time_since_click >= 10:
            self.score -= 0.10
            self.refresh_ui()
        # Schedule this function to run again in 1000ms (1 second)
        self.root.after(1000, self.update_idle)       


if __name__ == "__main__":
    root = tk.Tk()
    game = IdleClicker(root)
    root.mainloop()

