for t in range(int(input())):
    m = int(input())
    ans = [0]
    x = 0
    for i in range(m):
        p1, p2 = map(int, input().split())
        x += p1 - p2
        ans.append(x)

    print(-min(ans))
