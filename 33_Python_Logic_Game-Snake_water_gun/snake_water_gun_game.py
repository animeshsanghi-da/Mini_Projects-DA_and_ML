import random

# Display welcome message and rules
print("\n", "=" * 35, "\n  Welcome to Snake Water Gun Game!\n", "=" * 35, "\n")

# Snake beats Water, Water beats Gun, Gun beats Snake
game_dict = {"s": 1, "w": -1, "g": 0}
reverse_game_dict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get user input and make it lowercase to handle "S", "W", "G" safely
your_entry = input("Enter your choice (s/w/g): ").lower()

# Input Validation
if your_entry not in game_dict:
    print("\nInvalid input! Please enter 's', 'w', or 'g'.\n\n", "=" * 35)
else:
    your_choice = game_dict[your_entry]
    computer_choice = random.choice([-1, 0, 1])

    print(f"\nYou chose {reverse_game_dict[your_choice]}.")
    print(f"Computer chose {reverse_game_dict[computer_choice]}.\n")

    # The Math Magic: Deciding the winner
    if computer_choice == your_choice:
        print("---> Wooooow! It's a Draw.\n\n", "=" * 35)
    elif (computer_choice - your_choice) in [-1, 2]:
        print("---> Ohhhhhh! You Lost.\n\n", "=" * 35)
    else:
        print("---> Congrats! You Won.\n\n", "=" * 35)

# Idea behind the math:
'''
computer... you...  result...   (computer - you)
s(1)...     g(0)... you win      1
w(-1)...    s(1)... you win     -2  
g(0)...     w(-1)...you win      1

g(0)...     s(1)... you lose    -1
s(1)...     w(-1)...you lose     2
w(-1)...    g(0)... you lose    -1
'''