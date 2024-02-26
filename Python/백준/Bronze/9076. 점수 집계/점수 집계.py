for _ in range(int(input())):
    n = list(map(int, input().split()))
    n.sort()
    s = sum(n[1:4])

    if n[3] - n[1] < 4:
        print(s)
    else:
        print("KIN")
