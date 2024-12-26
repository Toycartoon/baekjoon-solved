n = int(input())
l = []

for i in range(n):
    a, h = map(int, input().split())

    l.append((a, h))


l.sort(key=lambda x: (x[0], -x[1]))
ans = 0

for i in range(1, n):
    ans = max(ans, abs(l[i][1] - l[i-1][1]))


print(ans)
