from math import gcd

n = int(input())
a = list(map(int, input().split()))
g = gcd(*a)

for i in range(1, g+1):
    if g % i == 0:
        print(i)
