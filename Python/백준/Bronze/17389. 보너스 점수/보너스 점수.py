n = int(input())
s = input()

ans = 0
b = 0
for i in range(n):
    if s[i] == "O":
        ans += i+1 + b
        b += 1
    elif s[i] == "X":
        b = 0

print(ans)
