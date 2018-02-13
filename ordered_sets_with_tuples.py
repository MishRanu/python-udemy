t = "a", "b", "c"

print(t)
print("a", "b", "c")
print({"a", "b", "c"})

welcome = "Welcome to the Nightmare", "Alice Cooper", 1975
bad = 'Bad Comany', "Bad Company", 1974
budgie = "Budgie", "Budgies", 1984

print(welcome)
print(welcome[1])

budgie = "Piece of papers", "Pickwick Company", 1981
budgie = budgie[0], "Anurag", budgie[2], welcome[1]
print(budgie)
#This assignment gives the error 'tuple' object does not support item assignment
#but i can reassign budgie with an item of the same type, which is good
#only that i cannot reassign items of the budgie because it is a set. Great!
# budgie[0] = "Budgies are back"

#Tuple is an immutable object, whereas a list is a mutable object. You cannot change the exisitng objects, but you can reassign it

#tuples are itended to hold items of different type in contreast to a list
#tuples can make it easier to remove bugs from your program and make your task easier


a = b = c = d = 12
print(c)

a, b = 12, 13
print(a, b)

a, b = b, a
#the right hand assignment is calculated and evaluated first
print(a, b)
#Nice

title, artist, year = welcome
print(title)
print(artist)
print(year)

#You can directly assign values to the variables from the tuples

#tuple can have elements that are actually tuples

# imelda = "More mayhem", "Imdelda May", 2011 , {1, "Pulling the Rug"}, {2, "Pyscho"}, {3, "Mayhem"}
# imelda = "More mayhem", "Imdelda May", 2011 , {1, "Pulling the Rug", 2, "Pyscho", 3, "Mayhem"}
imelda = "More mayhem", "Imdelda May", 2011 , { (1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem")}

# title, artist, year, track1, track2, track3 = imelda
print(imelda)
# print(track1)

#Nice
