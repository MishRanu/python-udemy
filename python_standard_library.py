#there is no such thing as private variable in python
#_ indicates private varibale in a module, and is not intended to be changed

#there are a lot of built in functions in python from the default build in imports


# print(dir())
#
# for m in dir(__builtins__):
#     print(m)


import shelve

# print(dir())
# print()
# print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != "_":
        print(obj)


# shelve.Shelf. <--- intellij help
import random
help(shelve)

help(random.randint)