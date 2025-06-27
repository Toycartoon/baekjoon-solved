import sys

input = sys.stdin.readline

while True:
    a, b = map(int, input().split())

    if a == b == 0:
        break

    f, g = set(), set()
    for i in range(a):
        f.add(int(input()))

    for i in range(b):
        g.add(int(input()))

    print(len(f & g))