from math import ceil

n = int(input())
a = list(map(int, input().split()))

print(max(0, ceil(n / 2) - a.count(1)))
