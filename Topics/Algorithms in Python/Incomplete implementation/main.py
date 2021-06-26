def startswith_capital_counter(names):
    total = 0
    for name in names:
        if name == "":
            continue
        if name is None:
            continue
        elif name[0] in "abcdefghijklmnopqrstuvwxyz".upper():
            total += 1
    return total

