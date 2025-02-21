import sys

input = sys.stdin.readline

l = []
for i in range(int(input())):
    l.append(int(input()))

if max(l) == l[0]:
    print("S")
else:
    print("N")
