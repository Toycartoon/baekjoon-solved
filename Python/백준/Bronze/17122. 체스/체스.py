for t in range(int(input())):
    s, n = input().split()

    if ((int(n)-1) // 8) % 2 == 0:
        if int(n) % 2 == 0:
            b = "B"
        else:
            b = "W"
    else:
        if int(n) % 2 == 0:
            b = "W"
        else:
            b = "B"

    if s[0] in "ACEG":
        if int(s[-1]) % 2 == 0:
            a = "B"
        else:
            a = "W"
    else:
        if int(s[-1]) % 2 == 0:
            a = "W"
        else:
            a = "B"

    print("YES" if a == b else "NO")
