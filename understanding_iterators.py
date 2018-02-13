# Any object that supports iterations is iterable, and we have discussed two such items till now: List and Strings

string = "123456789"

for char in string:
    print(char)

# we are going to make our own iterator

print("Check my own iterator")
myIterator = iter(string)
print(next(myIterator))
print(next(myIterator))

# for loop ueses next to get the next element and terminates when next() finally gives error when there are not elements to iterate

for char in iter(string):
    print(char)

# nice Nice

# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.


print("Now solving the udemy challenge problem")

numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbersListIterator = iter(numbersList)

for i in range(0, len(numbersList)):
    nextNumber = next(numbersListIterator)
    print(nextNumber)