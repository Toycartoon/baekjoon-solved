from math import lcm

n = int(input())
l = []
for x in list(map(int, input().split())):
    l.append(x * 2)


print(lcm(*l))
