

import random

secret = random.randint(1, 10)
attempts = 0

print("Guess the number (1 to 10)")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed it at {attempts} attempts")
        break
