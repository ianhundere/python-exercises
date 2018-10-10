import random

secretNumber = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

while not guess == secretNumber:
    if guess < 1 or guess > 10:
        print("Input a number from 1 to 10")
    guess = int(input("Guess a number between 1 and 10: "))

print("You guessed right!")
