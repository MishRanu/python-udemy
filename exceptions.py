#we are going to looking into exceptions and exception handling in python in this code
#new python file examples

def factorial(n):
    #can also be defined as n times n-1 factorial

    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

try:
    print(factorial(900))
except (RecursionError, ZeroDivisionError):
    print("This program does not calculate factorials that large")
except ZeroDivisionError:
    print("What are you doing divided by zero")

print("program terminating")