n = int(input())
g = [set() for _ in range(n+1)]
g[0].add(0)

for i in range(n):
    for x in g[i]:
        for w in (1, 5, 10, 50):
            g[i+1].add(x+w)

print(len(g[-1]))
