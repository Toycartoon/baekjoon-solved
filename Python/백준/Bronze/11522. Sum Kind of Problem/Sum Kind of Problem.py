import sys

input = sys.stdin.readline

for t in range(int(input())):
    k, n = map(int, input().split())

    print(k, n * (n + 1) // 2, n * (2 + (n - 1) * 2) // 2, n * (4 + (n - 1) * 2) // 2)
