import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b = input().strip().split()

    print("Distances:", end=" ")
    for i in range(len(a)):
        x, y = a[i], b[i]

        d = ord(y) - ord(x)

        if d < 0:
            d += 26

        print(d, end=" ")
    print()