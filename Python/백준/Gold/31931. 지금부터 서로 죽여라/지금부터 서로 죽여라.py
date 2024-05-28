import sys

input = sys.stdin.readline

for t in range(int(input())):
    x, y = map(int, input().strip().split())
    a, b, c, d = map(int, input().strip().split())

    if y <= a:
        print("NARUTO")
    elif b >= c and d >= a:
        print("DRAW")
    elif b >= c and d < a:
        if b > c:
            print("NARUTO")
        elif b == c:
            s = (x + c - 1) // c
            n = (y + a - 1) // a
            if n <= s:
                print("NARUTO")
            else:
                print("DRAW")
    elif b < c and d >= a:
        if d > a:
            print("SASUKE")
        elif d == a:
            s = (x + c - 1) // c
            n = (y + a - 1) // a
            if s < n:
                print("SASUKE")
            else:
                print("DRAW")
    elif b < c and d < a:
        s = (x + c - 1) // c
        n = (y + a - 1) // a
        if n <= s:
            print("NARUTO")
        else:
            print("SASUKE")
