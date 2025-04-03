for t in range(int(input())):
    ans = 0
    e, n = map(int, input().split())

    for i in range(n):
        if int(input()) > e:
            ans += 1

    print(ans)
