import sys

input = sys.stdin.readline

while True:
    try:
        n, b, m = map(float, input().split())

        ans = 0
        while n < m:
            n += (n / 100.0) * b
            ans += 1

        print(ans)
    except ValueError:
        break