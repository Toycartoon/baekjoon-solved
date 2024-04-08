from collections import deque


n = int(input())
d = deque(list(map(int, input().split())))
idx = deque([str(i) for i in range(1, n+1)])

ans = []
while d:
    x = d.popleft()
    ans.append(idx.popleft())

    if x > 0:
        d.rotate(-(x-1))
        idx.rotate(-(x-1))
    else:
        d.rotate(-x)
        idx.rotate(-x)

print(" ".join(ans))
