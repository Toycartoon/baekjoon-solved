import sys

input = sys.stdin.readline

n = int(input())
g = []
for i in range(n):
    t, gt = map(int, input().split())
    g.append((t, gt))


g.sort(key=lambda x: x[0])
ans = 0
for i in g:
    if ans < i[0]:
        ans = sum(i)
    else:
        ans += i[1]


print(ans)
