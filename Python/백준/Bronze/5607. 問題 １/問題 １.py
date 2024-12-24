import sys

input = sys.stdin.readline

a, b = 0, 0
for i in range(int(input())):
    x, y = map(int, input().split())

    if x > y:
        a += x + y
    elif x < y:
        b += x + y
    else:
        a += x
        b += y


print(a, b)
