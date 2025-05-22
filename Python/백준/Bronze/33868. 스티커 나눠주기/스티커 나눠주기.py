g = []
for n in range(int(input())):
    t, b = map(int, input().split())
    g.append((t, b))

g.sort(key=lambda x: -x[0])
t = g[0][0]

g.sort(key=lambda x: x[1])
b = g[0][1]

print((t * b) % 7 + 1)
