for t in range(int(input())):
    n = int(input())
    x, y = 0, 0
    s = input()

    for i in s:
        match i:
            case "E":
                x += 1
            case "W":
                x -= 1
            case "N":
                y += 1
            case "S":
                y -= 1

    print(abs(x) + abs(y))
