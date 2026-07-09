from random import randint

print("\n", "=" * 40, "\n   Welcome to the Number Guessing Game!\n", "=" * 40, "\n")

n = randint(1, 100)
a = 0
guesses = 1

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

print("\n" + "=" * 45)
print(f"🎉 Congratulations! You guessed the number {n} correctly in {guesses} attempts.")
print("=" * 45 + "\n")