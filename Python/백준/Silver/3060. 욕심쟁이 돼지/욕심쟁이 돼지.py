import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    x = sum(list(map(int, input().split())))
    ans = 1

    while n >= x:
        x *= 4
        ans += 1

    print(ans)
