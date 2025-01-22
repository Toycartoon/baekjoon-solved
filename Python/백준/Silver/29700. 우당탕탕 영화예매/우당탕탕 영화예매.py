import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
ans = 0

for i in range(n):
    g = [*input().strip()]

    for x in range(m-k+1):
        if set(g[x:x+k]) == {"0"}:
            ans += 1


print(ans)
