while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    a = list(map(int, input().split()))

    ans = 0
    for i in a:
        ans += min(i, m // n)

    print(ans)
