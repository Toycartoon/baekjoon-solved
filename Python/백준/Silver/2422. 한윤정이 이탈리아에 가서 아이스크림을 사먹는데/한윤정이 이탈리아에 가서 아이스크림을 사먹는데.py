n, m = map(int, input().split())

w = {}
for i in range(1, n+1):
    w[i] = set()

for i in range(m):
    x, y = map(int, input().split())
    w[x].add(y)
    w[y].add(x)


ans = 0
for a in range(1, n+1):
    for b in range(a+1, n+1):
        for c in range(b+1, n+1):
            if len(w[a]-{b, c}) == len(w[a]) and len(w[b]-{a, c}) == len(w[b]) and len(w[c]-{a, b}) == len(w[c]):
                ans += 1

print(ans)
