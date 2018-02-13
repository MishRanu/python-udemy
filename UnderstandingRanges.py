myRange = range(10)
print(myRange)

myList = list(range(10))
print(myList)

even = list(range(0,10,2))
odd = list(range(1,10, 2))
print("even {}".format(even))
print("odd {}".format(odd))

myString="abcdefgh"
print(myString.index('e'))
print(myString[4])

odd2 = range(1, 100000, 2)
print(odd2)

print(odd2[998])

# sevens = range(7, 10000, 7)
# x = int(input("Please enter a number less than 10000 \n"))
# if x in sevens:
#     print("{} is divisible by seven".format(x))

decimals = range(0, 100)

myDecimalsRange = decimals[3:40:3]
print(myDecimalsRange)

for i in myDecimalsRange:
    print(i)

print("#"*40)

for i in range(3, 40, 3):
    print(i)

print(myDecimalsRange==range(3,40,3))
#Technicaly they are equal. This is in stark constrast with Java which compares the object references for comparison

#In contrast, Python actually compares the order of the elements inside the element which is pretty cool
#I have always been a lazy coder and want instant gratification and produce something of good value
#producing with java takes some time but python is actually fun and pretty lenient
# I seem to like the language and there is pretty much everything under the sun that i can accomplish using python

#so i am going to expertise in Spring, Java and JSPs for good money for enterprise development
#But work in python for personal enjoyment, cool scripts, my own group, things that give me pleasure
#Finally i am starting to start and produce something of value
#Discrete mathematiccs, algorithms, and the power of python is all that i need to create the difference i want to create
# it is going to be fun, really exciting fun.
#Yeah i am going to do it.

#Moving on to some more useful information on Ranges


print(range(0, 5, 2)==range(0,6,2))
#obviously the sequence of elements is importance and that's why they equated to equal. Test for equality

r = range(0,100)

for i in r[::-2]:
    print(i)

for i in r[99: 0: -2]:
    print(i)

print("=="*50)

#For negative slicing the sequence definitely has to start in opposite order. A negative slice can be extremely useful

backString = "asdfasdfa adasdfasdf as asdfassdf"
print(backString)

print(backString[::-1])
#Yeah finally success
#Slicing is good. I like slicing. Coding is great.

