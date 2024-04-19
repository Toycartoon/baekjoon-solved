n = int(input())
a = list(map(int, input().split()))


def binary_search(l, r, i):
    while l < r:
        mid = (l + r) // 2

        if i > dp[mid]:
            l = mid + 1
        elif dp[mid-1] < i <= dp[mid]:
            return mid
        else:
            r = mid - 1

    return l


dp = [a[0]]
idx = [(len(dp)-1, a[0])]
i = 1
for i in range(1, n):
    if dp[-1] < a[i]:
        dp.append(a[i])
        idx.append((len(dp)-1, a[i]))
    else:
        pos = binary_search(0, len(dp)-1, a[i])
        idx.append((pos, a[i]))
        dp[pos] = a[i]


x = len(dp)-1
lis = []
for i in range(len(idx)-1, -1, -1):
    if idx[i][0] == x:
        lis.append(idx[i][1])
        x -= 1

print(len(dp))
print(*lis[::-1])
