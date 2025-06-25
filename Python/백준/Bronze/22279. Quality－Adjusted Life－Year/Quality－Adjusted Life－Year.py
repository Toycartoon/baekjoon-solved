ans = 0
for n in range(int(input())):
    q, y = map(float, input().split())
    ans += q * y

print(ans)
