n = int(input())
s = input()
w = {"J": "O", "O": "I", "I": "J"}

ans = ""
for i in s:
    ans += w[i]

print(ans)
