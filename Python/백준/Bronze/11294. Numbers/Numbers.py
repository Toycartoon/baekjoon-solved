while True:
    s = input()

    if s == "#":
        break

    b = int(input())
    x = int(input())
    n = x
    a = ""

    while n >= b:
        m = n % b
        n //= b

        if m < 10:
            a += str(m)
        else:
            a += chr(m + 55)

    m = n % b
    if m < 10:
        a += str(m)
    else:
        a += chr(m + 55)

    print(f"{s}, {x}, {a[::-1]}")
