n = int(input())
a, pa, b, pb = map(int, input().split())

mx = 0
ans = (0, 0)
for i in range(n+1):
    v = (a * (i // pa) + b * ((n - i) // pb))
    if v > mx:
        mx = v
        ans = (i // pa, (n - i) // pb)

print(*ans)
