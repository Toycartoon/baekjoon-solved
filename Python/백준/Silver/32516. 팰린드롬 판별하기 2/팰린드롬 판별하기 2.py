n = int(input())
s = input()

ans = 0
for i in range(n // 2):
    if s[i] != s[n-i-1]:
        if s[i] != "?" and s[n-i-1] != "?":
            print(0)
            exit()
        else:
            ans += 1
    elif s[i] == s[n-i-1] == "?":
        ans += 26


print(ans)
