#A set in python is unordered and doesn't contain duplicates, and items are accessed by a key, like in a dictionary
#sets are usually less ued but can be particuka

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("="*40)

wild_animals = set(["lion", "tiger", "panther", "elephant"])

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

empty_set = set()
empty_set_2 = {}
empty_set.add("a")
# empty_set_2.add("a")

# even = set(range(0,40,2))
# print(even)
# squares_tuple = {4, 6, 9, 16, 25}
# print(squares_tuple)
# squares = set(squares_tuple)
# print(squares)

even = set(range(0,40,2))
print(even)
print(len(even))


squares_tuple = (4,9, 16,25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print("="*40)

print(even.intersection(squares))
print(even&squares)
print(squares.intersection(even))
print(squares&even)


#now let us use the sort method before printing the elements out
# A-B removes any elements from set B that might be in Set A

print(sorted(even))
print(sorted(squares))

#difference and minus gives the same result, but the tim recommmends difference such that we explictly know that we are working with sets

print(sorted(even.difference(squares)))
print(sorted(even-squares))
print(sorted(squares.difference(even)))
print(squares-even)

even.difference_update(squares)
print(sorted(even))

even = set(range(0,40, 2))
print("symmetric even minus squares")
#notice that it includes 9 and 25, and the result if the same for both of them
#also that you could see this is like the union of the two sets minus the interesction of the two sets
#also notice that the output is sorted. We are not sure about whether the behavior is same for pther implementations in python

print(sorted(even.symmetric_difference(squares)))
print(sorted(squares.symmetric_difference(even)))
# print(sorted(squares.symmetric_difference_update(even)))

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
#remove if the element doesn't exist throws an error but discard doesn't throw such an error
# squares.remove(8)

if 8 in squares:
    squares.remove(8)

#remove is good when you want to throw an error when something illegal is taking place, like trying to remove an item doesn't exist

try:
    squares.remove(8)
except KeyError:
    print("the element 8 is not present in the squares set")

#you can also create list from a set using list() operator

squares_tuple2 = (4, 6, 16)
squares2 = set(squares_tuple2)
if squares2.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares2):
    print("even is the superset of squares")

#a frozen set is an immutable key, so we can use it as a key of the dictionary. once created, there is no add element to add elements to the set

even = frozenset(range(0,40,2))
print(even)
# even.add(1)
