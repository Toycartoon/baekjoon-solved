from collections import deque

q = deque([*"SciComLove"])
q.rotate(-int(input()))
print("".join(q))