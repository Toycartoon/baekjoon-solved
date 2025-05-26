n = int(input())
s = input()
ans = 0

for i in s:
    ans += ord(i) - 64

print(ans)
