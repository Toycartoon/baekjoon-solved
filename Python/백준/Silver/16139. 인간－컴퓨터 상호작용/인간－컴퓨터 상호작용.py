import sys

input = sys.stdin.readline

s = input().strip()
q = int(input())
pre_sum = []
alpha = [0] * 26
for i in s:
    alpha[ord(i)-97] += 1
    pre_sum.append(list(alpha))

for _ in range(q):
    a, l, r = input().split()

    l, r = int(l), int(r)
    if l == 0:
        print(pre_sum[r][ord(a)-97])
    else:
        print(pre_sum[r][ord(a)-97] - pre_sum[l-1][ord(a)-97])
