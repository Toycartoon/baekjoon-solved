n = int(input())
a = list(map(int, input().split()))

ans = 0
j = 1
for i in range(n-1):
    if a[i] >= a[i+1]:
        ans += j * (j+1) // 2
        j = 1
    else:
        j += 1


ans += j * (j+1) // 2
print(ans)
