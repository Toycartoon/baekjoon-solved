n = int(input())
g = []
v = [False for _ in range(n)]

for i in range(n):
    g.append(sorted([*input()]))

ans = 0
for x in range(n):
    if v[x]:
        continue

    v[x] = True
    for i in range(x+1, n):
        if g[x] == g[i]:
            v[i] = True
    ans += 1

print(ans)
