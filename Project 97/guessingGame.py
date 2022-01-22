import random

randomNumber=random.randint(1,9)
chances=0


while chances<5:
    Guess=int(input("Guess the number: "))
    chances=chances+1

    if Guess==randomNumber:
        print("Congratulations You Guessed Correctly")
    else:
        print("Close, guess again.")

if chances==5:
    print("You have lost.")
    print(randomNumber)