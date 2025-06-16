n = int(input())
ans = 0
for i in range(n):
    s = input()
    ans += pow(int(s[:-1]), int(s[-1]))

print(ans)
