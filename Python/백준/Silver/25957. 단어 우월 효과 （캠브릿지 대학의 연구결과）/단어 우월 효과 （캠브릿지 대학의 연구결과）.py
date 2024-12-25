import sys

input = sys.stdin.readline

w = {}
for n in range(int(input())):
    a = input().strip()
    w[("".join(sorted([*a])), a[0], a[-1])] = a


m = int(input())
for i in input().strip().split():
    print(w[("".join(sorted([*i])), i[0], i[-1])], end=" ")
