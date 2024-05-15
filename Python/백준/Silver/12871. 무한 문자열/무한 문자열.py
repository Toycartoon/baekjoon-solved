from math import lcm

s = input()
t = input()

l = lcm(len(s), len(t))
print(int(s * (l // len(s)) == t * (l // len(t))))
