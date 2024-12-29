import sys

input = sys.stdin.readline

l = []

for n in range(int(input())):
    l.append(float(input()))

l.sort()

for i in range(7):
    print("%.3f" % l[i])