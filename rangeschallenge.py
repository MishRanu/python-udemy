# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like.
#
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)

# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.

val = range(-1, -100, 4)
print(val)

print(len(val))

valN = range(-1, -100, -4)
print(len(valN))

# for i in valN:
#     print(i)

for i in valN[::-2]:
    print(i)

print(valN[::-2])
#Yeah see the step size is 4*2 = 8. The step size is 8. Nice!
#counting the elements in reverse

menu=[]
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["egg", "bacon", "sausage", "bacon", "spam"])

for item in menu[::-2]:
    print(item)
    print(item[::-2])
