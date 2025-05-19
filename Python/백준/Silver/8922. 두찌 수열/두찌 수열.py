import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = set()
    s.add(tuple(a))

    z = False
    while True:
        b = []
        for i in range(n):
            b.append(abs(a[i] - a[i+1 if i+1 < n else 0]))

        if b.count(0) == n:
            z = True
            break
        elif tuple(b) in s:
            break

        s.add(tuple(b))
        a = b

    if z:
        print("ZERO")
    else:
        print("LOOP")
