from math import lcm

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = lcm(sum(a), sum(b))
print(k // sum(a), k // sum(b))
