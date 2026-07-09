# Project 33: Snake Water Gun Game

Welcome to the Snake Water Gun project! This is a simple, command-line implementation of the classic "Rock-Paper-Scissors" game, re-themed with a logic-based twist.

## Overview

This Python script allows a user to play a game of Snake, Water, and Gun against the computer. The program uses a dictionary-based mathematical approach to determine the winner, rather than long `if-else` chains.

## How to Play

1. Ensure you have [Python](https://www.python.org/) installed on your system.
2. Clone or download this repository.
3. Open your terminal or command prompt.
4. Navigate to the directory containing the file:
   ```
   cd minor_projects/33_Python_Logic_Game-Snake_water_gun/
   ```
5. Run the game:
   ```
   python snake_water_gun_game.py
   ```
6. Follow the on-screen prompts to enter 's' (Snake), 'w' (Water), or 'g' (Gun).

## The "Math Magic" Behind the Game

Instead of comparing every possible outcome using multiple conditional statements, this project utilizes a clean numerical system:

* **Snake**: 1
* **Water**: -1
* **Gun**: 0

By calculating the difference between the computer's choice and your choice (`computer_choice - your_choice`), the game determines the result mathematically:

| Scenario | Result Logic |
| :--- | :--- |
| **Draw** | `computer_choice == your_choice` |
| **You Lose** | `(computer_choice - your_choice)` is in `[-1, 2]` |
| **You Win** | All other cases |

## Project Structure

* `snake_water_gun_game.py`: The main source code containing the game logic and user interface.

## Requirements

* Python 3.x
* No external libraries are required (uses the built-in `random` module).

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.