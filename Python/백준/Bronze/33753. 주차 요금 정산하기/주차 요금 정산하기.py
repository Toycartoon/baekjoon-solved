from math import ceil

a, b, c = map(int, input().split())
t = int(input())

if t <= 30:
    print(a)
else:
    print(a + (ceil((t-30) / b) * c))