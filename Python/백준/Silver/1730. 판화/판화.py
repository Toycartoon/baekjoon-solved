n = int(input())
s = input()

g = [["."] * n for _ in range(n)]
x, y = 0, 0
for i in s:
    if  i == "D" and 0 <= x < n and 0 <= y + 1 < n:
        if g[y][x] == ".":
            g[y][x] = "|"
        elif g[y][x] == "-":
            g[y][x] = "+"

        y += 1
        if g[y][x] == ".":
            g[y][x] = "|"
        elif g[y][x] == "-":
            g[y][x] = "+"
    elif i == "U" and 0 <= x < n and 0 <= y - 1 < n:
        if g[y][x] == ".":
            g[y][x] = "|"
        elif g[y][x] == "-":
            g[y][x] = "+"

        y -= 1
        if g[y][x] == ".":
            g[y][x] = "|"
        elif g[y][x] == "-":
            g[y][x] = "+"
    elif i == "L" and 0 <= x - 1 < n and 0 <= y < n:
        if g[y][x] == ".":
            g[y][x] = "-"
        elif g[y][x] == "|":
            g[y][x] = "+"

        x -= 1
        if g[y][x] == ".":
            g[y][x] = "-"
        elif g[y][x] == "|":
            g[y][x] = "+"
    elif i == "R" and 0 <= x + 1 < n and 0 <= y < n:
        if g[y][x] == ".":
            g[y][x] = "-"
        elif g[y][x] == "|":
            g[y][x] = "+"

        x += 1
        if g[y][x] == ".":
            g[y][x] = "-"
        elif g[y][x] == "|":
            g[y][x] = "+"

for i in g:
    print("".join(i))
