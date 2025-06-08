from math import inf

while True:
    n = int(input())

    if n == 0:
        break

    a = list(map(int, input().split()))
    a.sort()

    ans = inf
    for i in range(1, n):
        ans = min(ans, a[i]-a[i-1])

    print(ans)
