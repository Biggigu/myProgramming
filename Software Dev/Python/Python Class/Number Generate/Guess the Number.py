from random import (randint)

randomNumber = randint(1, 10)
chances = 3

while chances > 0:
    userSaid = int(input("I will generate a number between 1 and 10, can you guess the number? "))

    if userSaid == randomNumber:
        print("Correct! You've guessed the number.")
        break
    else:
        chances -= 1
        if chances > 0:
            print(f"Incorrect guess. You have {chances} chance(s) left. Try again.")
        else:
            print("Sorry, you've used all your chances. Better luck next time!")
            print(f"The correct number was {randomNumber}.")
