import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = [0]
    for i in range(n):
        a.append(int(input()))

    visited = [False for _ in range(n+1)]
    ans = 0

    x = 1
    f = False
    while not visited[x]:
        if x == n:
            f = True
            break
        visited[x] = True

        x = a[x]
        ans += 1

    if f:
        print(ans)
    else:
        print(0)
