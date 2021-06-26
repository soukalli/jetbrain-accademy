digits = input()
print([sum([int(x) for x in digits[:i]]) for i in range(1, len(digits) + 1)])
