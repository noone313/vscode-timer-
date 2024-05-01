import tkinter as tk
from tkinter import messagebox
import time
import pyautogui


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Timer")

        self.label = tk.Label(root, text="Time Elapsed: 0 seconds", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_time = None
        self.running = False

        # Start the timer automatically when the program starts
        self.start_timer(None)

        # Add a button to stop the timer
        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer)
        self.stop_button.pack(pady=10)

    def start_timer(self, event):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.update_timer()

    def stop_timer(self):
        if self.running:
            self.running = False
            elapsed_time = time.time() - self.start_time
            messagebox.showinfo("Timer Stopped", f"Elapsed Time: {elapsed_time:.2f} seconds")

    def update_timer(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.label.config(text=f"Time Elapsed: {elapsed_time:.2f} seconds")
            self.root.after(100, self.update_timer)  # Schedule the next update after 100 milliseconds


def main():
    root = tk.Tk()
    app = TimerApp(root)

    # Open vscode using pyautogui
    time.sleep(1)
    pyautogui.press('winleft')
    time.sleep(2)
    pyautogui.write('vs code')
    time.sleep(1)
    pyautogui.press('enter')

    # Delay to allow vscode to open
    time.sleep(5)

    root.mainloop()


if __name__ == "__main__":
    main()
