digits = input()
print([(int(digits[i]) + int(digits[i + 1])) / 2 for i in range(len(digits) - 1)])
