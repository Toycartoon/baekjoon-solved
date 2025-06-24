from math import ceil

a, b = map(int, input().split())
d = int(input())
print(ceil(a * b / 12) * d)
