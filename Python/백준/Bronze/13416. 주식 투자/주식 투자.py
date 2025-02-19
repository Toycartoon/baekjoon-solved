import sys

input = sys.stdin.readline

for t in range(int(input())):
    ans = 0
    for n in range(int(input())):
        a, b, c = map(int, input().split())
        ans += max(0, a, b, c)

    print(ans)
