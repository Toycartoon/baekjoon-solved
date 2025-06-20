for c in range(int(input())):
    n = int(input())

    ans = 0
    for i in range(1, n+1):
        if n % i == 0:
            ans += 1

    print(n, ans)
