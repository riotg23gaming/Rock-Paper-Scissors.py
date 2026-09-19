# Rock Paper Scissors

This is a console-based Rock Paper Scissors game that I built with Python while learning the basics of programming.

I wanted to make something a little more complete than a simple exercise, so I added things like score tracking, input validation, a replay option, computer reactions, and game history.

## About the Project

The game is played against the computer. At the beginning, the player chooses how many wins are needed to decide the winner.

For example, if you choose 3, the first player to reach 3 wins wins the game.

The player can choose:

* Rock
* Paper
* Scissors

The usual rules apply:

* Rock beats Scissors
* Paper beats Rock
* Scissors beats Paper
* Choosing the same move results in a draw

## Features

The game currently includes:

* First-to-N wins
* Player and computer score tracking
* Turn counter
* Input validation
* Option to quit during a game
* Random computer moves
* Computer thinking animation
* Random computer reactions
* Sound effects for wins and losses
* Game score history
* Option to start another game

## Technologies Used

The project was written in Python 3 and uses the following built-in modules:

* `random` for the computer's moves and random reactions
* `time` for delays and the thinking animation
* `winsound` for sound effects on Windows

No external Python packages are required.

## Requirements

You need:

* Python 3
* Windows, because the project uses the `winsound` module

## How to Run

Clone the repository:

```bash
(https://github.com/riotg23gaming/Rock-Paper-Scissors.py/edit/main/README.md)```

Move into the project folder:

```bash
cd rock-paper-scissors-python
```

Run the program:

```bash
python rock_paper_scissors.py
```

You can also open the project in an IDE such as PyCharm and run the Python file from there.

## How It Works

When the program starts, it asks how many wins are needed:

```text
How many wins are needed to decide the winner? : 3
```

The game then starts and asks the player to choose a move.

The computer generates its own move randomly. The program compares the two moves and increases the appropriate score.

The game continues until either the player or the computer reaches the required number of wins.

The player can also type `Quit` to leave the current game.

## Game History

The program keeps the final score of each game in a list of dictionaries.

For example:

```python
[
    {'Player': 3, 'COM': 2},
    {'Player': 1, 'COM': 3}
]
```

Each dictionary represents the result of one game.

## What I Practiced

This project gave me a chance to practice several Python concepts that I had been learning separately.

These include:

* Variables
* `if`, `elif`, and `else`
* `while` and `for` loops
* Lists
* Dictionaries
* User input
* String methods
* Random values
* `break` and `continue`
* f-strings
* Working with Python modules

One of the main things I learned from this project was how these basic concepts can be combined to create a complete program.

## Why I Made This

I made this project as part of my Python learning journey.

Instead of only working on small exercises, I wanted to build something that I could actually run and play. It also helped me practice debugging my own code and understanding how loops, conditions, and variables interact with each other.

The project is still written at a beginner level, and there are things I would probably structure differently as I learn more Python. For now, I wanted to keep it understandable and use concepts that I already know.

## Possible Improvements

There are several things I could add or improve in the future, for example:

* Better formatting for the game history
* Player statistics
* Difficulty levels
* Saving the history to a file
* Moving repeated code into functions
* A graphical version of the game

For now, I consider this project finished as a beginner Python project.

## Author

Yozdzhan Angelov

This project is part of my ongoing Python learning and practice.
