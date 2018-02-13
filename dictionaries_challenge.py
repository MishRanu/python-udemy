# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.

location = {0: "You are staring at the damn screen",
            1: "Baner road",
            2: "Dmart crossing",
            3: "vasant vihar",
            4: "sky fitness",
            5: "pashan"
            }


exits = {0: {"Q":0},
         1:{"W":2, "E": 3, "N":5, "S": 4, "Q": 0},
         2: {"W": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W":2, "Q":0},
         5: {"W": 2, "S": 1, "Q": 0}
}

input_directions = {
    "W": "W",
    " W": "W",
    "/nW": "W",
    "/nW/n": "W",
    "WEST/n": "W",
    "WEST": "W",
    "N": "N",
    " N": "N",
    "/nN": "N",
    "N/n": "N",
    "NORTH": "N",
    "NORTH/n": "W",
    "S": "S",
    " S": "S",
    "/nS": "S",
    "S/n": "S",
    "SOUTH": "S",
    "SOUTH/n": "W",
    "E": "E",
    " E": "E",
    "/nE": "E",
    "E/n": "E",
    "EAST": "E",
    "EAST/n": "W"
}

loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():
        availableExits += direction

    print(location[loc])

    if(loc==0):
        break

    direction = input_directions[input("Available exits are \n" + availableExits).upper()]
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")

