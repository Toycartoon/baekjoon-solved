x, y = map(int, input().split())
g = [x / y]
for n in range(int(input())):
    xi, yi = map(int, input().split())
    g.append(xi / yi)

print(round(min(g) * 1000, 2))
