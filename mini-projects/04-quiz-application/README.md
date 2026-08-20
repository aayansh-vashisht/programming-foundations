# 🧠 Quiz Application

A terminal-based Quiz Application built in Python that dynamically loads question banks, evaluates user answers with input validation, and provides detailed end-of-game score analytics.

---

## 🚀 Features

- 📂 **Separation of Data & Logic**: Questions and options are stored separately in `questions.json`, keeping the core code clean and extensible.
- 🛡️ **Input Validation**: Rejects invalid menu choices and forces the user to input allowed options without crashing.
- 📊 **Score & Percentage Tracking**: Calculates the final score and exact percentage after every round.
- 🔁 **Replay Option**: Allows players to immediately restart a new round or exit cleanly.

---

## 📁 File Structure

```text
├── questions.json   # External questions dataset
├── quiz_app.py      # Core quiz runner and CLI interface
└── README.md        # Project documentation
```

---

## 🛠️ Requirements

- **Python 3.6+**
- Standard Python libraries (`json`, `os`) — *no external dependencies required!*

---

## 📦 How to Run

1. Navigate to the project directory:
   ```bash
   cd mini-projects/04-quiz-application
   ```

2. Run the application:
   ```bash
   python quiz_app.py
   ```

---

## 🖥️ Example Usage

```text
=== QUIZ APPLICATION ===

Question 1: What is the correct file extension for Python files?
  A) .pt
  B) .py
  C) .pyt
  D) .pw
Your answer: b
✓ Correct!

Question 2: Which keyword is used to define a function in Python?
  A) func
  B) def
  C) function
  D) define
Your answer: x
Invalid input. Please choose from: A, B, C, D
Your answer: b
✓ Correct!

==============================
Quiz Finished!
Score: 4/4
Percentage: 100.0%
==============================

Do you want to play again? (y/n): n
Thanks for playing! Goodbye.
```
