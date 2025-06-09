while True:
    try:
        n, k = map(int, input().split())
        ans = n

        while n // k:
            ans += n // k
            n = n % k + n // k

        print(ans)
    except EOFError:
        break
