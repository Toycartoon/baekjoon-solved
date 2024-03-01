from math import factorial

for t in range(int(input())):
    s = input().split("!")
    n = 0
    f = False
    a, b = 0, 0
    for i in s:
        if i != "":
            n = int(i)
            f = True
        else:
            if f:
                b += 1
            else:
                a += 1

    for i in range(b):
        b -= 1
        n = factorial(n)

    for i in range(a):
        a -= 1
        n = int(not n)

    print(n)
