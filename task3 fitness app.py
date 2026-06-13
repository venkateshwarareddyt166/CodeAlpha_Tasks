import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ==========================
# DATABASE SETUP
# ==========================
conn = sqlite3.connect("fitness_tracker.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fitness (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    steps INTEGER,
    workout TEXT,
    duration INTEGER,
    calories INTEGER
)
""")

conn.commit()

# ==========================
# SAVE DATA FUNCTION
# ==========================
def save_data():
    try:
        steps = int(steps_entry.get())
        workout = workout_entry.get()
        duration = int(duration_entry.get())
        calories = int(calories_entry.get())

        cursor.execute(
            "INSERT INTO fitness (steps, workout, duration, calories) VALUES (?, ?, ?, ?)",
            (steps, workout, duration, calories)
        )
        conn.commit()

        messagebox.showinfo("Success", "Fitness Data Saved!")

        steps_entry.delete(0, tk.END)
        workout_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)
        calories_entry.delete(0, tk.END)

        update_dashboard()

    except:
        messagebox.showerror("Error", "Please enter valid data")

# ==========================
# DASHBOARD UPDATE
# ==========================
def update_dashboard():

    cursor.execute("""
    SELECT
    SUM(steps),
    SUM(duration),
    SUM(calories)
    FROM fitness
    """)

    result = cursor.fetchone()

    total_steps = result[0] if result[0] else 0
    total_duration = result[1] if result[1] else 0
    total_calories = result[2] if result[2] else 0

    steps_label.config(text=f"Total Steps: {total_steps}")
    duration_label.config(text=f"Workout Minutes: {total_duration}")
    calories_label.config(text=f"Calories Burned: {total_calories}")

    goal = 10000

    progress = min((total_steps / goal) * 100, 100)

    progress_bar["value"] = progress

# ==========================
# MAIN WINDOW
# ==========================
root = tk.Tk()
root.title("Fitness Tracker App")
root.geometry("700x650")
root.configure(bg="#f4f4f4")

# ==========================
# TITLE
# ==========================
title = tk.Label(
    root,
    text="Fitness Tracker Dashboard",
    font=("Arial", 22, "bold"),
    bg="#f4f4f4"
)
title.pack(pady=15)

# ==========================
# INPUT FRAME
# ==========================
frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="x")

tk.Label(frame, text="Steps Walked", bg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)

steps_entry = tk.Entry(frame, width=30)
steps_entry.grid(row=0, column=1)

tk.Label(frame, text="Workout Type", bg="white", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)

workout_entry = tk.Entry(frame, width=30)
workout_entry.grid(row=1, column=1)

tk.Label(frame, text="Workout Duration (min)", bg="white", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)

duration_entry = tk.Entry(frame, width=30)
duration_entry.grid(row=2, column=1)

tk.Label(frame, text="Calories Burned", bg="white", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)

calories_entry = tk.Entry(frame, width=30)
calories_entry.grid(row=3, column=1)

save_btn = tk.Button(
    frame,
    text="Save Activity",
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    command=save_data
)
save_btn.grid(row=4, column=0, columnspan=2, pady=15)

# ==========================
# DASHBOARD
# ==========================
dashboard = tk.Frame(root, bg="white", bd=2, relief="ridge")
dashboard.pack(padx=20, pady=15, fill="x")

tk.Label(
    dashboard,
    text="Progress Summary",
    font=("Arial", 16, "bold"),
    bg="white"
).pack(pady=10)

steps_label = tk.Label(
    dashboard,
    text="Total Steps: 0",
    font=("Arial", 12),
    bg="white"
)
steps_label.pack(pady=5)

duration_label = tk.Label(
    dashboard,
    text="Workout Minutes: 0",
    font=("Arial", 12),
    bg="white"
)
duration_label.pack(pady=5)

calories_label = tk.Label(
    dashboard,
    text="Calories Burned: 0",
    font=("Arial", 12),
    bg="white"
)
calories_label.pack(pady=5)

# ==========================
# PROGRESS BAR
# ==========================
tk.Label(
    root,
    text="Daily Step Goal Progress (10000 Steps)",
    font=("Arial", 12, "bold"),
    bg="#f4f4f4"
).pack(pady=10)

progress_bar = ttk.Progressbar(
    root,
    orient="horizontal",
    length=500,
    mode="determinate"
)
progress_bar.pack(pady=10)

# ==========================
# FOOTER
# ==========================
footer = tk.Label(
    root,
    text="Track • Improve • Achieve",
    font=("Arial", 10, "italic"),
    bg="#f4f4f4"
)
footer.pack(pady=15)

update_dashboard()

root.mainloop()

conn.close()