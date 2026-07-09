# Project 32: Number Guessing Game

This project is a simple command-line based logic game written in Python. It challenges the user to guess a randomly generated number between 1 and 100, providing feedback on each attempt.

## Features
- **Randomized Logic**: Uses Python's `random` module to generate a unique target number each time the game runs.
- **Input Validation**: Prevents invalid inputs outside the 1–100 range.
- **Dynamic Hints**: Automatically tells the player whether to guess a higher or lower number.
- **Attempt Tracking**: Counts and displays the total number of attempts taken to reach the correct answer.

## Requirements
- Python 3.x installed on your machine.

## How to Run
1. Ensure you have Python installed.
2. Open your terminal or command prompt.
3. Navigate to the folder containing `guess_the_number.py`.
4. Execute the script with the following command:

```
python guess_the_number.py
```

## Gameplay Instructions
1. When prompted, enter a number between 1 and 100.
2. If your guess is too low, you will see a prompt: "📈 Guess a higher number."
3. If your guess is too high, you will see a prompt: "📉 Guess a lower number."
4. If your guess is outside the allowed range, a warning will appear.
5. The game concludes once you guess the number correctly.

## Code Snippet
The core loop of the game is handled by the following logic:

```
while n != a:
    a = int(input(f"Attempt {guesses} | Guess a number between 1 and 100: "))
    
    if a < 1 or a > 100:
        print("⚠️ Out of bounds! Please guess a number inside the 1 to 100 range.\n")
        continue
    elif a < n:
        print("📈 Guess a higher number.\n")
        guesses += 1
    elif a > n:
        print("📉 Guess a lower number.\n")
        guesses += 1
```

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.