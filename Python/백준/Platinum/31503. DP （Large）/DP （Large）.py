import sys

input = sys.stdin.readline

n, q = map(int, input().split())
d = list(map(int, input().split()))


def binary_search(l, r, i, dp):
    while l < r:
        mid = (l + r) // 2

        if dp[mid] < i:
            l = mid + 1
        elif dp[mid-1] < i <= dp[mid]:
            return mid
        else:
            r = mid - 1

    return l


dp1 = [1]
lis = [d[0]]
for i in range(1, n):
    if lis[-1] < d[i]:
        lis.append(d[i])
        dp1.append(len(lis))
    else:
        idx = binary_search(0, len(lis)-1, d[i], lis)
        dp1.append(idx+1)
        lis[idx] = d[i]

d.reverse()
for i in range(n):
    d[i] = -d[i]

dp2 = [1]
lis = [d[0]]
for i in range(1, n):
    if lis[-1] < d[i]:
        lis.append(d[i])
        dp2.append(len(lis))
    else:
        idx = binary_search(0, len(lis)-1, d[i], lis)
        dp2.append(idx+1)
        lis[idx] = d[i]


for _ in range(q):
    a = int(input())
    print(dp1[a-1] + dp2[n-a] - 1)
