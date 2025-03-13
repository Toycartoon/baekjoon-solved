while True:
    n, *a = list(map(int, input().split()))

    if n == 0:
        break

    ans = [a[0]]
    for i in range(1, n):
        if ans[-1] != a[i]:
            ans.append(a[i])

    print(*ans, "$")
