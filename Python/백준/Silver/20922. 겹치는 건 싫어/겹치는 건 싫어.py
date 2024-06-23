n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 0
arr = [0] * (max(a) + 1)

ans = []
while r < n:
    if arr[a[r]] < k:
        arr[a[r]] += 1
        r += 1
    else:
        arr[a[l]] -= 1
        l += 1

    ans.append(r-l)

print(max(ans))
