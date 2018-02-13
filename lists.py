# # ipAddress = input("Please enter your ip address: ")
# # print(ipAddress.count("."))
#
# parrot_list = ["man_panin", "nore more", "a stiff", "bereft of live"]
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# print(numbers)
# #the idea behind sort method or function is the idea behind the sort method
# #works on the object and doesnot actually create a new object
# #the method sort actually mutates the objects
# #numbers.sort()
# print(numbers)
# #the method sorted actually returns the new object
#
# numbersInOrder = sorted(numbers)
# if numbers  == numbersInOrder:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#
# if numbersInOrder == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#

list_1 = []
list_2 = list()

print("List 1 : {}".format(list_1))
print("List 2 is {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal")


#All list types in python are iterable

print(list("The lists are equal"))
#Nice
even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
if even == another_even:
    print(even)
#both even and another_even refers to the same list and this can actually be confussing

another_even2=list(even)
another_even2.sort()
if even==another_even2:
    print("The lists are equal")
else:
    print("The lists are not equal")

odd = [1, 3, 5, 7, 9]
numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)