import sys

input = sys.stdin.readline

while True:
    s = input().strip()

    if s == "#":
        break

    for i in s.split():
        if len(i) == 1:
            print(i, end=" ")
        else:
            print(i[0] + i[1:-1][::-1] + i[-1], end=" ")
    print()
