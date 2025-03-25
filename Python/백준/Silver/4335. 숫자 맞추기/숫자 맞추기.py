import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    s = input().strip()
    l, r = 1, 10
    f = True
    while s != "right on":
        if s == "too high":
            r = min(n - 1, r)
        elif s == "too low":
            l = max(n + 1, l)

        if l > r:
            f = False

        n = int(input())
        s = input().strip()

    if f and l <= n <= r:
        print("Stan may be honest")
    else:
        print("Stan is dishonest")
