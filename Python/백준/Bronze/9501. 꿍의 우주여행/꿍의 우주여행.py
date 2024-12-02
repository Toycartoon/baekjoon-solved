import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, d = map(int, input().split())

    ans = 0
    for i in range(n):
        v, f, c = map(int, input().split())

        if v * (f / c) >= d:
            ans += 1

    print(ans)
