for t in range(int(input())):
    n, p, q = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    ans = 0
    w = 0
    for i in range(min(n, p)):
        if a[i] + w <= q:
            ans += 1
            w += a[i]
        else:
            break

    print(f"Case {t+1}: {ans}")
