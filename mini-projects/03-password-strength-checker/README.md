# 🔐 Password Strength Checker

A lightweight, CLI-based Password Strength Checker built in Python. This tool evaluates user passwords based on core security guidelines and provides detailed feedback without storing or logging any sensitive inputs.

---

## 🚀 Features

- 📏 **Length Check**: Validates if the password meets the minimum length requirement (8+ characters).
- 🔤 **Case Sensitivity**: Checks for both uppercase (`A-Z`) and lowercase (`a-z`) characters.
- 🔢 **Digit Verification**: Ensures the presence of numeric digits (`0-9`).
- 🔣 **Special Characters**: Checks for symbols (e.g., `!@#$%^&*`).
- 📊 **Strength Rating**: Classifies passwords as **Weak**, **Medium**, or **Strong** with an itemized checklist.
- 🔒 **Privacy Focused**: Passwords are processed temporarily in memory and are **never saved or written to files**.

---

## 🛠️ Requirements

- Python 3.x
- Standard Python libraries (`string`) — *no external dependencies required!*

---

## 📦 How to Run

1. Navigate to the project directory:
   ```bash
   cd mini-projects/03-password-strength-checker
