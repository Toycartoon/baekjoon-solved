from collections import deque
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
a = deque(map(int, input().split()))

for i in range(q):
    com, x, *s = map(int, input().split())

    if com == 1:
        a[x-1] += s[0]
    elif com == 2:
        a.rotate(x)
    elif com == 3:
        a.rotate(-x)


print(*a)
