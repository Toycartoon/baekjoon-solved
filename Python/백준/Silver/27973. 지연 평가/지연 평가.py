import sys

input = sys.stdin.readline

a = 1
m = 1
d = 0
_n = 0
for _ in range(int(input())):
    c, *n = map(int, input().split())

    if c == 0:
        a += n[0]
        d += n[0]
    elif c == 1:
        a *= n[0]
        m *= n[0]
        d *= n[0]
    elif c == 2:
        _n += n[0]
        a = (m * _n) + m + d
    else:
        print(a)