a, b = map(int, input().split())
arr = [i for i in range(b+1)]

arr[1] = 0
for i in range(2, int(len(arr) ** 0.5)+1):
    if arr[i] == 0:
        continue
        
    for j in range(i * i, b+1, i):
        arr[j] = 0


s = []
for i in arr:
    if i == 0:
        continue
    else:
        s.append(i)

ans = 0
for x in range(a, b+1):
    l = []
    idx = 0
    while x != 1 and idx < len(s):
        if x % s[idx] == 0:
            l.append(i)
            x //= s[idx]
        else:
            idx += 1
    
    if arr[len(l)] != 0:
        ans += 1


print(ans)