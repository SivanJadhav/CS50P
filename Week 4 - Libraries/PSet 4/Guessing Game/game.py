from random import randint
import sys

while True:
    level = input("Level: ")

    try:
        level = int(level)
        if level < 1:
            pass
        else:
            break
    except ValueError:
        pass


while True:

    randnum = randint(1, level)

    guess = input("Guess: ")

    try:
        guess = int(guess)

        if guess < randnum:
            print("Too small!")
        elif guess > randnum:
            print("Too large!")
        else:
            sys.exit("Just right!")

    except ValueError:
        pass
