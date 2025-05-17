n = int(input())
s = input()

ans = 0
for i in range(0, n, n // 10):
    if s[i:i+(n//10)].count("T") == n // 10:
        ans += 1

print(ans)
