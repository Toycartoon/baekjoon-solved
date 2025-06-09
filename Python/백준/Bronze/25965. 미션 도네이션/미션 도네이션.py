for n in range(int(input())):
    m = int(input())
    mx = []
    for i in range(m):
        mx.append(tuple(map(int, input().split())))

    k, d, a = map(int, input().split())

    ans = 0
    for x, y, z in mx:
        ans += max(0, x * k + a * z - d * y)

    print(ans)
