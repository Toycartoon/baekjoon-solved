n, k = map(int, input().split())
a = list(map(int, input().split()))

a.extend(a[::-1])

s = 0
for i in range(len(a)):
    if s <= k < s + a[i]:
        if i < n:
            print(i + 1)
            break
        else:
            print(n * 2 - i)
            break

    s += a[i]
