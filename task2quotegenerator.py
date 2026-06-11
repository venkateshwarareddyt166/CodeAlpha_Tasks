import tkinter as tk
import random

# List of quotes
quotes = [
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Do something today that your future self will thank you for.", "Sean Patrick Flanery"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("Push yourself, because no one else is going to do it for you.", "Unknown")
]

# Function to display a random quote
def show_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"— {author}")

# Main window
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("600x350")
root.configure(bg="white")

# Heading
title_label = tk.Label(
    root,
    text="Random Quote Generator",
    font=("Arial", 18, "bold"),
    bg="white"
)
title_label.pack(pady=20)

# Quote text
quote_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    wraplength=500,
    justify="center",
    bg="white"
)
quote_label.pack(pady=20)

# Author text
author_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "italic"),
    bg="white"
)
author_label.pack(pady=10)

# Button
new_quote_btn = tk.Button(
    root,
    text="New Quote",
    font=("Arial", 12, "bold"),
    command=show_quote,
    padx=15,
    pady=8
)
new_quote_btn.pack(pady=20)

# Show a quote when app starts
show_quote()

root.mainloop()