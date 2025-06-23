while True:
    n = int(input())

    if n == -1:
        break

    ans = 0
    temp = 0
    for i in range(n):
        s, t = map(int, input().split())
        ans += s * (t - temp)
        temp = t

    print(ans, "miles")
