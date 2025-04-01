for t in range(int(input())):
    n = int(input())
    w = sum(list(map(int, input().split())))

    if w > 0:
        print("Right")
    elif w < 0:
        print("Left")
    else:
        print("Equilibrium")