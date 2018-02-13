import shelve


bit  = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# with shelve.open('recipes') as recipes:
#     # recipes["bit"] = bit
#     # recipes["beans on toast"] = beans_on_toast
#     # recipes["scambled eggs"] = scrambled_eggs
#     # recipes["tin of soup"] = soup
#     # recipes["pasta"] = pasta
#
#     #we have written it in memory but never told the shelves to update it in the shelves
#     # recipes["blt"].append
#
#     temp_list = recipes["bit"]
#     temp_list.append("butter")
#     recipes["bit"] = temp_list
#
#     for snack in recipes:
#         print(snack, recipes[snack])

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["bit"] = bit
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scambled eggs"] = scrambled_eggs
    # recipes["tin of soup"] = soup
    # recipes["pasta"] = pasta

    #we have written it in memory but never told the shelves to update it in the shelves
    # recipes["blt"].append

    # temp_list = recipes["bit"]
    # temp_list.append("butter")
    # recipes["bit"] = temp_list

    recipes["bit"].append("margarines")

    for snack in recipes:
        print(snack, recipes[snack])
