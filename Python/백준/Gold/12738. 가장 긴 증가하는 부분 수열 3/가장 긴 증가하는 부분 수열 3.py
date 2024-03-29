n = int(input())
a = list(map(int, input().split()))

def binary_search(l, r, i):
    while l < r:
        mid = (l + r) // 2

        if i > lis[mid]:
            l = mid + 1
        elif lis[mid-1] < i <= lis[mid]:
            return mid
        else:
            r = mid - 1

    return l


lis = [a[0]]
i = 1
for i in range(1, n):
    if lis[-1] < a[i]:
        lis.append(a[i])
    else:
        pos = binary_search(0, len(lis)-1, a[i])
        lis[pos] = a[i]

print(len(lis))
