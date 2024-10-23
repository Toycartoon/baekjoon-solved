s = input()

ans = 0
for i in range(len(s)):
    if s[i] == "O":
        ans += 2 ** i

    ans %= (10 ** 9) + 7
    

print(ans)