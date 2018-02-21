def my_range(n:int):
    print("my range starts")
    start = 0
    while start < n:
        yield start
        start += 1

big_range = my_range(5)
big_list = []
print(big_range)
print(next(big_range))

for i in big_range:
    big_list.append(i)

print(big_range)
print(big_list)
"Continuing with big_range"
for x in big_range:
    print(x)