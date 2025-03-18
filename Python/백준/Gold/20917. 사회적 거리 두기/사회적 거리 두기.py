import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    l = 0
    r = a[-1] - a[0] + 1
    ans = 0
    while l + 1 < r:
        mid = (l + r) // 2

        x = 1
        j = 0
        for i in range(1, n):
            if a[i] - a[j] >= mid:
                x += 1
                j = i

        if x >= s:
            ans = max(ans, mid)
            l = mid
        else:
            r = mid

    print(ans)
