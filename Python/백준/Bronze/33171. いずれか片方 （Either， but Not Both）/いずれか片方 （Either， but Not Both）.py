n = int(input())
a = int(input())
b = int(input())

ans = 0
for i in range(1, n+1):
    if (i % a == 0 and i % b != 0) or (i % a != 0 and i % b == 0):
        ans += 1

print(ans)
