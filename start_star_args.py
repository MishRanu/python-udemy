#kwargs is to pack variable number of named arguments, or keyword arguments
#example of one of this is the print statement


def print_backwards(*args, end=' ', **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)

print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
