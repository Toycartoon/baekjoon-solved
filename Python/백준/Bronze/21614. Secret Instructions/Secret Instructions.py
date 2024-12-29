import sys

input = sys.stdin.readline

b = ""
while True:
    n = input().strip()

    if n == "99999":
        break

    if sum(map(int, [*n[:2]])) % 2 == 1:
        print("left", end=" ")
        b = "left"
    elif n[:2] == "00":
        print(b, end=" ")
    else:
        print("right", end=" ")
        b = "right"

    print(n[2:])
