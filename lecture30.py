name=input("Please enter your name ")
age=int(input("Please enter your age "))

if 18<age<31:
    print("Hi {}! You are welcome to the 18-30 holiday".format(name, age))
else:
    print("Sorry you cannot be granted entry. ")