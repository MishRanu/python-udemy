#storing large data in the memory is sometimes not feasible
#shelves can be used to store and data dictionaries, sort of like a persistent storage


import shelve

# with shelve.open("ShelfTest") as fruit:
#     fruit['orange'] = "a sweet orange fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour yellow cirtus fruit"
#     fruit['grape'] = "a small round sweet fruit"
#     fruit['lima'] = "a sour green cirtrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# print(fruit)
#shelve is by default read and write by nature
#shelve stores the data in a database and the database used depends on the underlying implementation

fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet orange fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour yellow cirtus fruit"
# fruit['grape'] = "a small round sweet fruit"
# fruit['lime'] = "a sour green cirtrus fruit"
#
# print(fruit["lemon"])
# print(fruit["grape"])
#
# while True:
#     shelf_key = input("Please enter a fruit: ")
#     if shelf_key == "quit":
#         break
#     if shelf_key in fruit:
#         description = fruit.get(shelf_key, "We don't have a " + shelf_key)
#         print(description)
#     else:
#         print("We don't have a " + shelf_key)


# ordered_keys = sorted(list(fruit.keys()))
#
# for f in ordered_keys:
#     print(f + " = " + fruit[f])
#


for v in fruit.values():
    print(v)

print(fruit.values())
for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()
print(fruit)