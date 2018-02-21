
def divide(n1, n2):
    try:
        return int(n1)/int(n2)
    except ZeroDivisionError:
        print("Division by zero is not valid and defined \n")
    except Exception:
        print("The division can not be calculated because of an exception")

n1 = input("Enter input number 1 \n")
n2 = input("Enter input number 2 \n")
print(divide(n1, n2))