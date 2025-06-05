n, m = map(int, input().split())
for _ in range(n):
    l = list(map(int, input().split()))

    for x in range(0, len(l), 3):
        r = l[x]
        g = l[x+1]
        b = l[x+2]

        i = 2126 * r + 7152 * g + 722 * b
        if i < 510000:
            print("#", end="")
        elif i < 1020000:
            print("o", end="")
        elif i < 1530000:
            print("+", end="")
        elif i < 2040000:
            print("-", end="")
        else:
            print(".", end="")
    print()
