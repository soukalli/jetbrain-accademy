n = int(input())
winners = [i[0] for i in [input().split() for _ in range(n)] if i[1] == "win"]
print(winners)
print(len(winners))
