for t in range(int(input())):
    s = input()
    l, d = s.split("-")

    n = 0
    for i in range(3):
        n += (ord(l[i]) - 65) * 26 ** (2 - i)
    print("nice" if abs(n - int(d)) <= 100 else "not nice")
