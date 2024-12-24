import sys

input = sys.stdin.readline

a = [0 for _ in range(10001)]
for n in range(int(input())):
    a[int(input())] += 1


print(a.index(max(a)))
