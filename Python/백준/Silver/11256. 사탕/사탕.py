import sys

input = sys.stdin.readline

for t in range(int(input())):
    j, n = map(int, input().split())
    g = []
    for i in range(n):
        r, c = map(int, input().split())
        g.append(r * c)

    g.sort(reverse=True)
    ans = 0
    for i in range(n):
        if j <= 0:
            break
        j -= g[i]
        ans += 1

    print(ans)
