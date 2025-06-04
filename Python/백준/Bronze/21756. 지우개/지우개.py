n = int(input())
g = [*range(1, n+1)]

while len(g) > 1:
    new_g = []
    for i in range(1, len(g), 2):
        new_g.append(g[i])

    g = new_g

print(g.pop())
