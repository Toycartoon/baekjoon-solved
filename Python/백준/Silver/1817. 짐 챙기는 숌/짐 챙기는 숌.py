n, m = map(int, input().split())

if n == 0:
    print(0)
    exit()
    
a = list(map(int, input().split()))

ans = 1
b = 0
for i in a:
    if b + i <= m:
        b += i
    else:
        b = i
        ans += 1

print(ans)
