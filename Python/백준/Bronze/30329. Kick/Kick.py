ans = 0
s = input()
for i in range(3, len(s)):
    if s[i-3:i+1] == "kick":
        ans += 1

print(ans)