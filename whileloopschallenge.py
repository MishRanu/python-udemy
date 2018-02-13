# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random
maxNumber = 10
randomNumber = random.randint(1, maxNumber)
guessNumber = int(input("Please guess the number "))

while(guessNumber!=randomNumber):
    print("Sorry you made the wrong guess \n")
    if(guessNumber < randomNumber):
        print("Plese guess higher \n")
    else:
        print("Please guess lower")
    guessNumber = int(input("Please re enter your guess \n"))
else:
    print("Congratulations! You have correctly guessed the number")
