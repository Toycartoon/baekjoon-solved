import sys

input = sys.stdin.readline

for t in range(int(input())):
    m, n, x, y = map(int, input().split())

    k = 0
    xset = set()
    yset = set()
    while min(m * k + x, n * k + y) <= m * n:
        xset.add(m * k + x)
        yset.add(n * k + y)
        k += 1

    ans = sorted(list(xset & yset))
    print(-1 if len(ans) == 0 else ans[0])
