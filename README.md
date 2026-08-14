# 🎮 Rock Paper Scissors Game

A simple command-line **Rock Paper Scissors** game built using Python. This project was created to practice Python basics, conditional logic, loops, user input, and the `random` module.

## 🚀 Features

### Version 1 — Basic Game

* Player chooses Rock, Paper, or Scissors
* Computer randomly selects a choice
* Determines the winner
* Handles tie conditions
* Validates the player's choice

### Version 2 — Score & Replay

* Keeps track of the player's score
* Keeps track of the computer's score
* Allows the player to play multiple rounds
* Displays the current score after each round
* Displays the final score when the player exits

## 🛠️ Technologies Used

* Python 3
* `random` module

## 📚 Concepts Practiced

* Variables
* Tuples
* User input with `input()`
* Conditional statements (`if`, `elif`, `else`)
* `while` loops
* Boolean conditions
* Functions from Python modules
* Random selection using `random.choice()`
* Score tracking
* Input validation
* String methods such as `.lower()`

## 🎯 Game Rules

The rules are:

* 🪨 **Rock beats Scissors**
* 📄 **Paper beats Rock**
* ✂️ **Scissors beats Paper**
* Same choices result in a **tie**

## ▶️ How to Run

1. Clone the repository.
2. Open the project folder in VS Code.
3. Run the Python file:

```bash
python rock_paper_scissors.py
```

4. Enter one of:

```text
rock
paper
scissors
```

5. The computer will randomly select its choice.
6. The winner will be displayed.

## 💻 Example

```text
Enter rock, paper, scissors: rock

Your choice: rock
Computer choice: scissors

You won!

Score - You: 1 | Computer: 0

Play again? (yes/no): no

Final Score - You: 1 | Computer: 0
Thanks for playing!
```

## 📁 Project Structure

```text
Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

## 🔮 Future Improvements

* Add a best-of-3 / best-of-5 mode
* Improve input validation
* Add a graphical interface using Tkinter
* Add difficulty levels
* Rebuild the game using Object-Oriented Programming (OOP)

## 👨‍💻 Author

**Vishal Kalva**

Built as a Python practice project to strengthen programming fundamentals.
