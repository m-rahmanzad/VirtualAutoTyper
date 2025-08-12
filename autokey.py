# -*- coding: utf-8 -*-
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

def start_typing():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "insert your text")
        return
    messagebox.showinfo("Info", "you have 5 second")
    root.withdraw()
    time.sleep(5)
    pyautogui.typewrite(text, interval=0.05)
    root.deiconify()

# make main panel
root = tk.Tk()
root.title("Virtual Auto Typer")
root.geometry("300x300")
root.resizable(False, False)  # don't resize

# label
label = tk.Label(root, text="insert your text", font=("Arial", 10))
label.pack(pady=(10, 5))

# text box
text_box = tk.Text(root, wrap=tk.WORD, font=("Arial", 10), height=10, width=30)
text_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# button
start_button = tk.Button(root, text="start", font=("Arial", 11), command=start_typing)
start_button.pack(pady=10, ipadx=10, ipady=5)

root.mainloop()
