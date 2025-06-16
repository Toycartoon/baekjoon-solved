n = int(input())
s = input()

g = []
for i in range(0, len(s), n):
    x = s[i:i+n]
    if (i // n) % 2 == 0:
        g.append([*x])
    else:
        g.append([*x[::-1]])

for i in zip(*g):
    print(*i, sep="", end="")
