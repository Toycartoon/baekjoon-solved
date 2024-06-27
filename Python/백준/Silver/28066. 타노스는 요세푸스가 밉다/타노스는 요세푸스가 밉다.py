from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])

while len(q) != 1:
    q.rotate(-1)
    for i in range(min(len(q)-1, k-1)):
        q.popleft()

print(q.popleft())
