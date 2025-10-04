# number guessing game
import random

computer_guess = random.randint(1,100)

status = True
while status:
    user_guess = int(input("Enter your guess : "))
    if user_guess > computer_guess:
        print("Hint : Guess lower Number")
    elif user_guess < computer_guess:
        print("Hint : Guess higher Number")
    else:
        print("Right Guess !!!!")
        status = False
