for t in range(int(input())):
    s = input()
    v, e = 0, 0
    for i in s:
        if i in "aeiou":
            v += 1
        else:
            e += 1

    print(s)
    if v <= e:
        print(0)
    else:
        print(1)
