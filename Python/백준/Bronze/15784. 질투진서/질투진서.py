n, a, b = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

x = g[a-1][b-1]
if max(g[a-1]) != x or max(list(zip(*g))[b-1]) != x:
    print("ANGRY")
else:
    print("HAPPY")
