import sys

input = sys.stdin.readline

n = input().strip()
w = [0 for _ in range(26)]

for i in n:
    w[ord(i) - 97] += 1

for i in range(int(input())):
    k = input().strip()

    l = [0 for _ in range(26)]
    for x in k:
        l[ord(x) - 97] += 1

    f = True
    for i in range(26):
        if l[i] > w[i]:
            f = False
            break

    if f:
        print(k)
