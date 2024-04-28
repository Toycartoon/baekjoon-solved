import sys
from collections import deque

input = sys.stdin.readline

l, r = deque([*input().rstrip()]), deque()

for m in range(int(input())):
    com, *val = input().split()

    if com == "L" and len(l) != 0:
        r.appendleft(l.pop())
    elif com == "D" and len(r) != 0:
        l.append(r.popleft())
    elif com == "B" and len(l) != 0:
        l.pop()
    elif com == "P":
        l.append(val[0])

print("".join(l) + "".join(r))
