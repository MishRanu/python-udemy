#in this section we will learning to write data in a file in a number of ways
#python dictionary objects offer a very useful name to store data

#when the file is being written to, it is very important to close the file toherwise the file might get corrupted

jabber = open("D:\\study\\python_exercise\\python-practice-workspace\\sample.txt", mode='r')


# for line in jabber:
#     print(line)
#
# jabber.close()

#Great, great, great never knew opening a file was so easy and flexible. Python is really incredible
#and one of the most powerful languages in the world
#i have to become wonderful at python and data structure and algorithms
# i am the man of the house and have to do it. Continously push, and improve
#I am on a hunter
#I am the apex predator. I cannot loose. I cannot lie down. I cannot lay down my guard. I have to work hard
# not just for myself but the entire world. I can only help people and redistribute resources only if i have them myself
#the single massive resource redistribution in this world

#you can give absolute as well as the relative path in the open window

#pythonic is called the python way of doing things, and this is an excellent of doing things in pythonic way

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()


with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "jab" in line.lower():
            print(line, end='')

#with will automatically handle any error that might come with opening and handling the file
#which is pretty cool, given our need to continuously working with files. it also automatically closes the file

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end="")
        line = jabber.readline()
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt") as jabber:
    lines_read = jabber.read()

for line_read in lines_read[::-1]:
    print(line_read, end='')

#read is recommeended to work with  binary file
#readLines will load the entire file in the memory and that can be an issue at times
