import sys

input = sys.stdin.readline

w, h = 0, 0
for i in range(int(input())):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    w = max(w, a)
    h = max(h, b)


print(w * h)
