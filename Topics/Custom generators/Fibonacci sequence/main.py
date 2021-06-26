def fibonacci(n):
    u = 0
    uu = 1
    for i in range(n):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            (u, uu) = (uu, u + uu)
            yield uu
