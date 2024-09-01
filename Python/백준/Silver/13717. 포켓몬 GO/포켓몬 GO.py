import sys

input = sys.stdin.readline

n = int(input())
p = []
ev = []
for _ in range(n):
    x = 0
    p.append(input().strip())
    k, m = map(int, input().split())

    while k <= m:
        if m >= k:
            m -= k
            x += 1
            m += 2

    ev.append(x)


print(sum(ev))
print(p[ev.index(max(ev))])
