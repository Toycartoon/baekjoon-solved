from math import ceil

n = int(input())
a = input().split()
b, c = map(int, input().split())

s = n
for i in range(n):
    s += ceil(max(0, (int(a[i]) - b)) / c)

print(s)