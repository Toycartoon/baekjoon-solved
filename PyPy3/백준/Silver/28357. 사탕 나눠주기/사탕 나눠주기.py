n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 10 ** 12
while l < r:
    mid = (l + r) // 2
    
    x = 0
    for i in a:
        if i > mid:
            x += i - mid
    
    if x > k:
        l = mid + 1
    else:
        r = mid


print(l)