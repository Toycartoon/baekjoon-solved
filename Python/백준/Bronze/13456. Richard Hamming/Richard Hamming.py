for t in range(int(input())):
    n = int(input())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if u[i] != v[i]:
            ans += 1

    print(ans)
