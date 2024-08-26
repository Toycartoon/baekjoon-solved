import sys

input = sys.stdin.readline

n, h = map(int, input().split())
d = list(map(int, input().split()))

ans = 0
for i in d:
    h -= i
    ans += 1

    if h <= 0:
        break


if h > 0:
    print(-1)
else:
    print(ans)
