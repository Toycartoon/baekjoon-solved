import sys

input = sys.stdin.readline

for t in range(int(input())):
    x, y = map(int, input().split())

    d = y - x

    if d == 0:
        print(0)
        continue

    ans = 0
    n = 1

    while True:
        if ans % 2 == 1:
            if n ** 2 < d <= n ** 2 + n:
                print(ans + 1)
                break
            n += 1
        else:
            if n * (n - 1) < d <= n ** 2:
                print(ans + 1)
                break

        ans += 1
