# 🔐 Password Strength Analyzer

A Python-based cybersecurity tool that evaluates password strength using multiple security checks, including password length, character complexity, common-password detection, predictability analysis, keyboard patterns, sequential characters, repetition, entropy, and a combined security score.

## 🎯 Project Objective

The objective of this project is to analyze passwords from a security perspective and identify patterns that may make them vulnerable to common password attacks.

The analyzer goes beyond simple character-count rules by checking for predictable and commonly used password patterns.

## 🛡️ Features

- 📏 Password length analysis
- 🔠 Uppercase character detection
- 🔡 Lowercase character detection
- 🔢 Number detection
- 🔣 Special character detection
- 🚫 Common-password detection
- 🧠 Predictability detection
- ⌨️ Keyboard-pattern detection
- 🔗 Sequential-character detection
- 🔁 Repeated-character detection
- 📊 Entropy calculation
- 🎯 Security score from 0–100
- 🔎 Combined security/correlation analysis
- 💡 Security recommendations
- 👁️ Password visibility toggle
- 🖥️ Graphical cybersecurity dashboard
- 🧪 Automated unit testing

## 🧠 Security Analysis

The analyzer evaluates multiple aspects of a password instead of relying only on length and character complexity.

It checks for patterns such as:

- Common passwords
- Predictable words
- Keyboard sequences such as `qwerty`
- Ascending or descending sequences
- Repeated characters
- Missing character categories

The results are combined to produce an overall security score.

## 📊 Entropy Analysis

The analyzer also calculates theoretical password entropy based on the character pools present in the password.

Entropy is reported in bits and is used as an additional security metric.

> Note: Entropy represents theoretical search-space complexity and does not directly represent the actual time required to crack a password.

## 🖥️ Graphical Dashboard

The project includes a modern dark-themed Tkinter dashboard that displays:

- 🔐 Password input
- 🎯 Circular security score
- 🛡️ Password strength classification
- 📊 Entropy
- 🔎 Individual security checks
- 💡 Security recommendations
- 👁️ Password visibility control
- ⚡ Analysis status indicator

## 📁 Project Structure

```text
PasswordStrengthAnalyzer/
│
├── core/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── patterns.py
│   ├── common_passwords.py
│   ├── correlation.py
│   └── suggestions.py
│
├── gui/
│   ├── __init__.py
│   └── dashboard.py
│
├── data/
│   ├── password_history.txt
│   └── common_passwords.txt
│
├── reports/
│
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
│
├── main.py
└── README.md
```

## ⚙️ Technologies Used

- Python
- Tkinter
- Python Standard Library
- unittest
- File-based password dataset

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/sanskruti0408/Password_Strength_Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd PasswordStrengthAnalyzer
```

### 3. Run the Application

```bash
python main.py
```

## 🧪 Running Tests

The project includes automated unit tests covering the core password analysis functionality.

Run:

```bash
python -m unittest discover -s tests -v
```

**Test Result**

```
Ran 17 tests

OK
```

All 17 automated tests passed successfully. ✅

## 🔍 Example Analysis

Example passwords used during testing include:

| Password       | Purpose                                  |
|-----------------|-------------------------------------------|
| password        | Common and predictable password           |
| qwerty123       | Keyboard and sequential pattern           |
| Password123!    | Complex but predictable                   |
| Abcdef12!       | Sequential pattern with complexity        |
| A1!b2@C3#       | Strong mixed-character password           |
| K7@mQ2!vR9      | Strong and less predictable password      |

## 🔒 Privacy

- Password analysis is performed locally by the application.
- Passwords entered into the analyzer are not intentionally transmitted to an external service.

## 🎓 Internship Project

- **Project:** Password Strength Analyzer
- **Domain:** Cyber Security & Ethical Hacking
- **Role:** Cyber Security Intern

This project was developed as part of a cybersecurity internship to demonstrate practical implementation of password security analysis techniques.

## 👩‍💻 Author

**Sanskruti Vharambale**

Diploma in Computer Engineering<br>
Cyber Security & Ethical Hacking
