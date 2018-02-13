# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

vowels_set = frozenset(('a', 'e', 'i', 'o', 'u'))
vowels_set2 = frozenset("aeiou")
print(vowels_set==vowels_set2)
text = input("Please enter the text \n")

finalSet = set(text).difference(vowels_set)
print(finalSet)
print(sorted(finalSet))

# answer = []
# for char in text:
#     if char not in vowels_set and char != ' ':
#         answer.append(char)
#
# print(answer)
# print(' '.join(sorted(answer)))
