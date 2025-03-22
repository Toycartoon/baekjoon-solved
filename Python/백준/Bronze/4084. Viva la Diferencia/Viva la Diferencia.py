import sys

input = sys.stdin.readline

while True:
    a, b, c, d = map(int, input().split())

    if a == b == c == d == 0:
        break

    ans = 0
    while len({a, b, c, d}) != 1:
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
        ans += 1

    print(ans)
