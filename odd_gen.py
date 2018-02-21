def odd_generator():
    current = -1
    while True:
        current += 2
        yield current

odds = odd_generator()
for i in range(101):
    print(next(odds))

