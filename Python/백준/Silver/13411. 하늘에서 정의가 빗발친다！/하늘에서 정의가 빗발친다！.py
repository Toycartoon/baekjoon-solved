from math import sqrt
import sys

input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    x, y, v = map(int, input().split())
    l.append((sqrt((x ** 2) + (y ** 2)) / v, i+1))

l.sort(key=lambda x: x[0])
for i in l:
    print(i[1])
