import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    f = False
    for i in range(1, 30):
        if k == (2 ** i):
            f = True
            break

    if f:
        print("GoHanGang")
    else:
        print("Gazua")
