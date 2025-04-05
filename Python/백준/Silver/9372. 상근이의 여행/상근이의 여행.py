import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    for _ in range(m):
        input()

    print(n-1)
