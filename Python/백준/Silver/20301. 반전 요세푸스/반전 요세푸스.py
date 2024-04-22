from collections import deque

n, k, m = map(int, input().split())
d = deque(i for i in range(1, n + 1))

i = 0
f = False
while len(d) != 0:
    if f:
        d.rotate(k)
    else:
        d.rotate(-k + 1)
    print(d.popleft())
    i += 1

    if i >= m:
        f = not f
        i = 0
