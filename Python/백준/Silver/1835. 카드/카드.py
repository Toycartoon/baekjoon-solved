from collections import deque

q = deque()
n = int(input())

for i in range(n, 0, -1):
    q.append(i)
    for x in range(i):
        q.rotate(-1)

print(*reversed(q))
