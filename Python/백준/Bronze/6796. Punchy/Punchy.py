import sys

input = sys.stdin.readline

a, b = 0, 0
while True:
    com, *vx = input().split()

    if com == "1":
        if vx[0] == "A":
            a = int(vx[1])
        elif vx[0] == "B":
            b = int(vx[1])
    elif com == "2":
        if vx[0] == "A":
            print(a)
        elif vx[0] == "B":
            print(b)
    elif com == "3":
        if vx[0] == vx[1] == "A":
            a += a
        elif vx[0] == "A" and vx[1] == "B":
            a += b
        elif vx[0] == "A" and vx[1].isnumeric():
            a += int(vx[1])
        elif vx[0] == "B" and vx[1] == "A":
            b += a
        elif vx[0] == vx[1] == "B":
            b += b
        elif vx[0] == "B" and vx[1].isnumeric():
            b += int(vx[1])
    elif com == "4":
        if vx[0] == vx[1] == "A":
            a *= a
        elif vx[0] == "A" and vx[1] == "B":
            a *= b
        elif vx[0] == "A" and vx[1].isnumeric():
            a *= int(vx[1])
        elif vx[0] == "B" and vx[1] == "A":
            b *= a
        elif vx[0] == vx[1] == "B":
            b *= b
        elif vx[0] == "B" and vx[1].isnumeric():
            b *= int(vx[1])
    elif com == "5":
        if vx[0] == vx[1] == "A":
            a -= a
        elif vx[0] == "A" and vx[1] == "B":
            a -= b
        elif vx[0] == "A" and vx[1].isnumeric():
            a -= int(vx[1])
        elif vx[0] == "B" and vx[1] == "A":
            b -= a
        elif vx[0] == vx[1] == "B":
            b -= b
        elif vx[0] == "B" and vx[1].isnumeric():
            b -= int(vx[1])
    elif com == "6":
        if vx[0] == vx[1] == "A":
            a //= a
        elif vx[0] == "A" and vx[1] == "B":
            a //= b
        elif vx[0] == "A" and vx[1].isnumeric():
            a //= int(vx[1])
        elif vx[0] == "B" and vx[1] == "A":
            b //= a
        elif vx[0] == vx[1] == "B":
            b //= b
        elif vx[0] == "B" and vx[1].isnumeric():
            b //= int(vx[1])
    elif com == "7":
        break
