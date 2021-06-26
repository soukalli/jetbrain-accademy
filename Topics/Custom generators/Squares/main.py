n = int(input())


def squares():
    i = 1
    while True:
        yield i ** 2
        i += 1


# Don't forget to print out the first n numbers one by one here
generator = squares()
for _ in range(n):
    print(next(generator))
