import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    ans = (m - n + 1) * (n + m) // 2

    print(f"Scenario #{t+1}:")
    print(ans)
    print()
