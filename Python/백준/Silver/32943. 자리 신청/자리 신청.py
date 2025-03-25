import sys

input = sys.stdin.readline

x, c, k = map(int, input().split())
g = [0 for _ in range(c+1)]
p = [0 for _ in range(x+1)]

q = []
for _ in range(k):
    t, s, n = map(int, input().split())
    q.append((t, s, n))

q.sort(key=lambda x: x[0])

for t, s, n in q:
    if g[s] == 0:
        g[s] = n
        if p[n] != 0:
            g[p[n]] = 0
        p[n] = s


for i in range(len(p)):
    if p[i] != 0:
        print(i, p[i])
