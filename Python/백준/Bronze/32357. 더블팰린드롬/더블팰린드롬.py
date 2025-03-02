from math import perm

n = 0
for i in range(int(input())):
    s = input()
    if s == s[::-1]:
        n += 1

print(perm(n, 2))
