import sys

input = sys.stdin.readline

g = []
for i in range(int(input())):
    g.append(int(input()))

g.sort(reverse=True)
ans = 0
for i in range(len(g)):
    if (i + 1) % 3 == 0:
        continue
    ans += g[i]

print(ans)
