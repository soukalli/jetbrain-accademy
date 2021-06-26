n = int(input())


def even():
    i = 0
    while True:
        yield 2 * i
        i += 1


# Don't forget to print out the first n numbers one by one here
generator = even()
for _ in range(n):
    print(next(generator))
