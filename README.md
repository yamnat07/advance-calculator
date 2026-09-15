# Advanced Calculator 🧮

A command-line calculator built in Python as an **upgraded version of my previous Basic Calculator project**.

This project represents my progress in learning Python. Compared with my earlier calculator, this version focuses more on **functions, input validation, loops, and exception handling**, making the program more structured and reliable.

**Previous project:** [Basic Calculator](https://github.com/yamnat07/basic-calculator)

---

## 🚀 My Progress

This project is the next step after my Basic Calculator.

### Basic Calculator → Advanced Calculator

| Basic Calculator | Advanced Calculator |
|---|---|
| Basic calculator functionality | More operations |
| Simple program structure | Separate functions for different tasks |
| Basic input handling | Input validation |
| Limited error handling | `try/except` exception handling |
| Basic calculation flow | Menu-based repeated calculations |
| Fewer checks for incorrect input | Validation for choices, numbers, and operators |
| Simple error situations | Handles `ZeroDivisionError` |

This project shows my progress from writing a simple working program toward writing a more organized and error-resistant Python program.

---

## ✨ Features

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`
- Remainder `%`
- Power `**`
- Validates menu choices
- Validates numeric input
- Validates supported operators
- Handles division by zero
- Allows multiple calculations
- Provides an option to exit

---

## 🧠 Concepts Used

### Functions
The program is divided into separate functions:

- `take_choice()`
- `take_num1()`
- `take_num2()`
- `take_op()`
- `calculate()`
- `main()`

This makes each part of the program responsible for a specific task.

### `while` Loops
Loops are used to keep asking for input until the user provides a valid value and to keep the calculator running until the user chooses to exit.

### Conditional Statements
`if`, `elif`, and `else` are used for:

- Menu selection
- Operator validation
- Selecting the correct calculation

### Exception Handling
The calculator uses `try/except` to handle errors without crashing.

For example:

```python
try:
    num1 = float(input("Enter first number: "))
except ValueError:
    print("Enter a valid value!!")
```

`ZeroDivisionError` is also handled when the user tries to divide by zero.

### Input Validation
The program checks whether:

- The menu choice is valid
- The entered numbers are valid
- The selected operator is supported

### Return Values
The input functions return valid values so they can be used by other functions.

### F-Strings
F-strings are used to display calculation results clearly.

---

## ▶️ How to Run

Make sure Python 3 is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/yamnat07/advanced-calculator.git
```

Move into the project directory:

```bash
cd advanced-calculator
```

Run the program:

```bash
python adv-calculator.py
```

---

## 💻 What Can a User Expect?

When the program starts, the user sees a menu:

```text
####################################
~~~~~~~~~ADVANCE CALCULATOR~~~~~~~~~
####################################

1.Do a calculation.
2.Exit.
```

Choosing **1** starts a calculation.

The program asks for:

```text
Enter first number:
Enter second number:
Enter the operator:
```

The user can then choose one of the supported operations.

For example:

```text
Enter first number: 10
Enter second number: 5
Enter the operator: +

The sum is: 15.0
```

If the user enters an invalid number, the program does not crash. It asks for a valid value again.

If an unsupported operator is entered, the program asks the user to enter a valid operator.

If the user attempts to divide by zero, the program catches the error and allows the calculation to be entered again.

---

## 📌 Supported Operations

| Operator | Operation | Example |
|---|---|---|
| `+` | Addition | `10 + 5 = 15` |
| `-` | Subtraction | `10 - 5 = 5` |
| `*` | Multiplication | `10 * 5 = 50` |
| `/` | Division | `10 / 5 = 2` |
| `%` | Remainder | `10 % 3 = 1` |
| `**` | Power | `10 ** 2 = 100` |

---

## 📚 Learning Goal

The goal of this project was to go beyond simply making a calculator work.

While building this version, I practiced:

- Breaking a program into functions
- Taking and validating user input
- Using `while` loops
- Using conditional statements
- Handling runtime errors with `try/except`
- Handling `ValueError`
- Handling `ZeroDivisionError`
- Improving the overall structure of a Python program

This project is part of my progression from a **Basic Calculator** toward more structured Python projects.

---

## 🔮 Future Improvements

Possible improvements for future versions include:

- Adding more mathematical operations
- Adding calculation history
- Adding advanced mathematical functions
- Improving the user interface
- Refactoring the calculation section to make it even more modular

---

## 👤 Author

**Yamnat07**

GitHub: [@yamnat07](https://github.com/yamnat07)