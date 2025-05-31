import sys

input = sys.stdin.readline

while True:
    n, *p = map(int, input().split())

    if n == 0:
        break

    ans = []
    p = p[0]

    if p % 2 == 0:
        ans.append(p-1)
        x = n - 2 * ((p // 2) - 1)
    else:
        ans.append(p+1)
        x = n - 2 * (((p+1) // 2) - 1)

    ans.append(x)
    ans.append(x-1)

    ans.sort()
    print(*ans)
