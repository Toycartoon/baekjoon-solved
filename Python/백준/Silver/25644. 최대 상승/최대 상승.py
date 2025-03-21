n = int(input())
a = list(map(int, input().split()))

ans = [0]
m = 10 ** 9
for i in range(n):
    if m > a[i]:
        m = a[i]
    else:
        ans.append(a[i]-m)

print(max(ans))
