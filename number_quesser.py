# a random number generator
import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range < 0:
        print("Please type a number")
        quit()
else:
    print("Please type a number")
    quit()
r = random.randint(0, top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess < 0:
            print("Please type a number")
            quit()
    else:
        print("Please type a number")
        continue
    if user_guess == r:
        print("you got it")
        break
    else:
        if user_guess > r:
            print("you were above the number")
        else:
            print("You are below the number")
print(f"you got it in {guess} guesses")
