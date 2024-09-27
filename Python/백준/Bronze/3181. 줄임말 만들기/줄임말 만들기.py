s = input().split()
ans = ""

for i in range(len(s)):
    if s[i] in ('i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili') and i != 0:
        continue
    ans += s[i][0]

print(ans.upper())
