import sys

input = sys.stdin.readline

while True:
    x, y, z = map(int, input().split())

    if x == y == z == 0:
        break

    s = input().strip()
    a = (x + y + z) % 25 + 1

    for i in s:
        if i.isalpha():
            v = ord(i) - a
            if v < 97:
                v += 26

            print(chr(v), end="")
        else:
            print(i, end="")
    print()
