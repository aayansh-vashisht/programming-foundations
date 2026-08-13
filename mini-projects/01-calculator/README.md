# Command-Line Calculator

A lightweight, interactive Python-based Command-Line Interface (CLI) calculator that supports continuous sequential arithmetic operations, state management, and robust input validation.

---

## 🚀 Features

- **Sequential Calculations**: Keeps track of the running total (`Current result`), allowing you to perform chain calculations seamlessly.
- **Core Arithmetic Operations**:
  - `+` Addition
  - `-` Subtraction
  - `*` Multiplication
  - `/` Division
- **State Controls**:
  - `c` (Clear): Resets the stored result back to `None` to start a fresh calculation.
  - `q` (Quit): Terminates the application safely.
- **Error Handling**:
  - **Division by Zero Protection**: Safely prevents program crash when attempting to divide by `0` and resets the current result.
  - **Input Validation**: Rejects invalid numeric inputs and unlisted operation prompts without crashing the program loop.

---

## 📋 Prerequisites

- **Python 3.6+** installed on your system. No external third-party dependencies are required.

---

## 📥 Installation & Setup

1. **Clone or Download** the repository to your local computer.
2. Ensure your script is saved as `calculator.py` (or your preferred file name).

---

## 🛠️ How to Run

Open your terminal or command prompt, navigate to the directory where the file is located, and execute:

```bash
python calculator.py

## 📂 Project Structure

```text
01-calculator/
│
├── calculator.py   # Main calculator program
└── README.md       # Project documentation


