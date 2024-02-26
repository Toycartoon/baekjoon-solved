import sys

input = sys.stdin.readline

l = []
for _ in range(int(input())):
    l.append(input().split())


l = sorted(sorted(l, key=lambda x: x[0]), key=lambda x: int(x[1]), reverse=True)
print(l[0][0])
