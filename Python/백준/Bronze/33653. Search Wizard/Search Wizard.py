w = input()
m = int(input())
s = input()

ans = 0
for i in range(len(w)-1, len(s)+1):
    if s[i-len(w):i] == w:
        ans += 1

print(ans)
