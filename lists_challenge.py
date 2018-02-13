# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13

menu=[]
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["egg", "bacon", "sausage", "bacon", "spam"])

for meal in menu:
    for item in meal:
        if item == "spam":
            break
    else:
        print("Here are the meals without spam in it")
        for item in meal:
            print(item)
else:
    print("Happy a happy meal!")