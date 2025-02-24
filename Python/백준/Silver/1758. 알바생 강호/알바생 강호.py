import sys

input = sys.stdin.readline

g = []
for i in range(int(input())):
    g.append(int(input()))

g.sort(reverse=True)
ans = 0

for i in range(len(g)):
    ans += max(0, g[i]-i)


print(ans)
