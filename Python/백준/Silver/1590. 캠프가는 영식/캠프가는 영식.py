import sys
from math import inf, isinf

input = sys.stdin.readline

ans = inf
n, t = map(int, input().split())
for _ in range(n):
    s, i, c = map(int, input().split())

    for v in range(s, s + i * c, i):
        if v >= t:
            ans = min(v-t, ans)
            break

print(ans if not isinf(ans) else -1)
