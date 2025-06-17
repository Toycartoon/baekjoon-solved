import sys

input = sys.stdin.readline

p = int(input())
for i in range(p):
    n, d, a, b, f = map(float, input().split())
    print(int(n), f * (d / (a + b)))
