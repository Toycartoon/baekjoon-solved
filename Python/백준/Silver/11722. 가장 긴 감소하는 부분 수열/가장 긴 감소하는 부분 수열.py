n = int(input())
a = list(map(int, input().split()))

def binary_search(l, r, i):
    while l < r:
        mid = (l + r) // 2

        if lis[mid] < i:
            l = mid + 1
        elif lis[mid-1] < i <= lis[mid]:
            return mid
        else:
            r = mid - 1

    return l


a.reverse()

lis = [a[0]]
for i in range(1, n):
    if lis[-1] < a[i]:
        lis.append(a[i])
    else:
        idx = binary_search(0, len(lis)-1, a[i])
        lis[idx] = a[i]


print(len(lis))
