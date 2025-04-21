import sys
from collections import deque

input = sys.stdin.readline

q = []
for i in range(int(input())):
    c = input().strip().split()

    if c[0] == "3":
        if len(q) != 0:
            q.pop()
    else:
        q.append(tuple(c))

ans = deque()
for i in q:
    if i[0] == "1":
        ans.append(i[1])
    elif i[0] == "2":
        ans.appendleft(i[1])

print("".join(ans) if len(ans) > 0 else 0)
