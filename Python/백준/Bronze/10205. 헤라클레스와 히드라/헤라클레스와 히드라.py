import sys

input = sys.stdin.readline

for k in range(int(input())):
    h = int(input())
    s = input().strip()

    for i in s:
        if i == "c":
            h += 1
        elif i == "b":
            h -= 1

        if h < 1:
            h = 0
            break

    print(f"Data Set {k+1}:")
    print(h)
    print()
