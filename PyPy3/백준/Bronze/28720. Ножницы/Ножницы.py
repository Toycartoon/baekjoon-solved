n, m = map(int, input().split())

ans = 0
v = n-1
for i in range(m-1):
    if v <= 0:
        break
        
    ans += v
    v -= 1

v = m-2
for i in range(n-1):
    if v <= 0:
        break

    ans += v
    v -= 1

print(ans)
