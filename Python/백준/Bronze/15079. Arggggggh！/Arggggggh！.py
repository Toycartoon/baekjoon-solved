n = int(input())
x, y = map(int, input().split())

for i in range(n-1):
    dir, d = input().split()
    s = ((int(d) ** 2) / 2) ** 0.5

    match dir:
        case "N":
            y += int(d)
        case "E":
            x += int(d)
        case "S":
            y -= int(d)
        case "W":
            x -= int(d)
        case "NE":
            y += s
            x += s
        case "SE":
            y -= s
            x += s
        case "SW":
            y -= s
            x -= s
        case "NW":
            y += s
            x -= s

print(x, y)
