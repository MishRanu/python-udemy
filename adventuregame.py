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

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING":"3",
              "VALLEY": "4",
              "FOREST": "5"
}
loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():
        availableExits += direction

    print(location[loc])

    if loc==0:
        break

    direction = input("Available exists are {} \n".format(availableExits)).upper();
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = word
                break
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")

