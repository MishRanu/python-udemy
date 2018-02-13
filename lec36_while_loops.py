# for i in range(10):
#     print("i is now {}".format(i))
#
# i = 0
# while i <10:
#     print(" i is now {}".format(i))
#     i += 1
#
# available_exits = ["east", "north-east", "south"]
#
# chosen_exit= ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("please choose a direction ")
#     if chosen_exit == "quit":
#         print("Game over")
#         break
# else:
#     print("aren't you glad that you got out of here")
#

import random
highest =10

answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess lower")
    else:
        print("Please guess higher")

    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you have not guessed correctly")
else:
    print("You got it right the first time")