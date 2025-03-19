import sys

input = sys.stdin.readline

for n in range(int(input())):
    s = int(input())
    x = input().strip()

    f = [False, False, False, False]
    if s < 12:
        print('invalid')
        continue

    for i in x:
        if i.isupper():
            f[0] = True
        elif i.islower():
            f[1] = True
        elif i.isdigit():
            f[2] = True
        elif i in "+_)(*&^%$#@!./,;{}":
            f[3] = True

    if f.count(True) == 4:
        print("valid")
    else:
        print("invalid")
