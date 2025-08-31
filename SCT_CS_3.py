import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length, bool(upper), bool(lower), bool(digit), bool(special)])

    if score == 5:
        return "Strong 💪"
    elif 3 <= score < 5:
        return "Moderate ⚠"
    else:
        return "Weak ❌"

# GUI Logic
def show_strength():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "Please enter a password!")
        return
    strength = check_password_strength(pwd)
    messagebox.showinfo("Password Strength", f"Password is: {strength}")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x180")
root.configure(bg="#2c2f33")

# Label
label = tk.Label(root, text="Enter Password:", fg="white", bg="#2c2f33", font=("Arial", 12))
label.pack(pady=10)

# Password entry
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

# Button
btn = tk.Button(root, text="Check Strength", command=show_strength, bg="#7289da", fg="white", font=("Arial", 12))
btn.pack(pady=15)

# Run the GUI
root.mainloop()