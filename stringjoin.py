myList = ["a", "b", "c", "d"]

newString = ", ".join(myList)
print(newString)
#I am very much impressed by this feature of python. Whoops all the elements of a string joined by a single line of code
#There cannot be a better utility language than this
#maybe i should code. Apart from mathematics it really interests me, and i can easilly do it for a long number of hours

letters = "aadfadsfasfasfasfasf"
newString = ", ".join(letters)

print(newString)

#now let us concatenate the keys of a dictionary

location = {0: "You are staring at the damn screen",
            1: "Baner road",
            2: "Dmart crossing",
            3: "vasant vihar",
            4: "sky fitness",
            5: "pashan"
}

exits =[{"Q":0},
        {"W":2, "E": 3, "N":5, "S": 4, "Q": 0},
        {"W": 5, "Q": 0},
        {"W": 1, "Q": 0},
        {"N": 1, "W":2, "Q":0},
        {"W": 2, "S": 1, "Q": 0}
]

loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():
        availableExits += direction

    print(location[loc])

    if(loc==0):
        break

    direction = input("Available exits are \n" + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
