import sys

input = sys.stdin.readline

s = set()
ans = 0
for n in range(int(input())):
    g = set(list(map(int, input().split())))

    if len(s & g) == 0:
        ans += 1
    s.update(g)

print(ans)
