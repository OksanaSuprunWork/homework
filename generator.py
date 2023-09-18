def number_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1
for num in number_generator(18, 37):
    print(num)