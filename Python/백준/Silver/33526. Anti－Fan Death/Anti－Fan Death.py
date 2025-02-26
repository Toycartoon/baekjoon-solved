from collections import deque

n = int(input())
x = ["Z", "N", "A"]
q = deque(x)
for i in range(3):
    for j in range(n):
        print("".join(q) * n)
    q.rotate(-1)
