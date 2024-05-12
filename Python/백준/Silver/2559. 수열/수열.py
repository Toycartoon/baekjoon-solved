import sys


input = sys.stdin.readline

n, k = map(int, input().split())
pre_sum = []

l = list(map(int, input().split()))
a = 0
for i in l:
    a += i
    pre_sum.append(a)


ans = []
for r in range(k-1, n):
    l = r - k + 1
    
    if l-1 < 0:
        ans.append(pre_sum[r])
    else:
        ans.append(pre_sum[r] - pre_sum[l-1])

print(max(ans))
