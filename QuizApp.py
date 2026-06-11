import tkinter as tk
from tkinter import messagebox

# Questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for Machine Learning?",
        "options": ["Python", "HTML", "CSS", "Photoshop"],
        "answer": "Python"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Bill Gates", "Elon Musk", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    }
]

current_question = 0
score = 0

# Window
root = tk.Tk()
root.title("Quiz App")
root.geometry("500x350")
root.resizable(False, False)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    wraplength=450
)
question_label.pack(pady=20)

selected_option = tk.StringVar()

radio_buttons = []

for i in range(4):
    rb = tk.Radiobutton(
        root,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 12)
    )
    rb.pack(anchor="w", padx=50)
    radio_buttons.append(rb)


def load_question():
    question_data = questions[current_question]

    question_label.config(
        text=f"Q{current_question + 1}. {question_data['question']}"
    )

    selected_option.set(None)

    for i, option in enumerate(question_data["options"]):
        radio_buttons[i].config(text=option, value=option)


def next_question():
    global current_question, score

    selected = selected_option.get()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select an answer."
        )
        return

    if selected == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        messagebox.showinfo(
            "Quiz Finished",
            f"Your Score: {score}/{len(questions)}"
        )
        root.destroy()


next_btn = tk.Button(
    root,
    text="Next",
    command=next_question,
    font=("Arial", 12)
)
next_btn.pack(pady=20)

load_question()

root.mainloop()