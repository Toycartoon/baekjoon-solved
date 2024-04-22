s = input()

ans = "z" * 50
for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        if s[:i][::-1] + s[i:j][::-1] + s[j:][::-1] < ans:
            ans = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]


print(ans)
