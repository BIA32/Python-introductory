tries = 0

import random

number = random.randint(1, 50)

print("I am thinking of a number between 1-50")

guess = int(input("Try to guess the number I am thinking of: "))

if guess > number:
    print("Too high, guess lower...")
elif guess<number:
    print("Too low, guess higher...")
elif guess==number:
    print("Congratulations, you got it correct.")
else:
    print("invalid argument....")

while guess!=number and tries<3:
    guess = input("Wrong number, Try Again.")
    guess = int(guess)
    tries+=1

if tries>5:
    print("Game over, you lose..... this is the correct number, ", number)