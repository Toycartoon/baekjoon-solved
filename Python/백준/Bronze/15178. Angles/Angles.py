for t in range(int(input())):
    n = list(map(int, input().split()))

    if sum(n) != 180:
        print(*n, "Check")
    else:
        print(*n, "Seems OK")