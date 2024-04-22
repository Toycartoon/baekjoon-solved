import sys
from collections import deque

input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    c, *v = map(int, input().split())

    if c == 1:
        q.appendleft(v[0])
    elif c == 2:
        q.append(v[0])
    elif c == 3:
        try:
            print(q.popleft())
        except:
            print(-1)
    elif c == 4:
        try:
            print(q.pop())
        except:
            print(-1)
    elif c == 5:
        print(len(q))
    elif c == 6:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif c == 7:
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif c == 8:
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
