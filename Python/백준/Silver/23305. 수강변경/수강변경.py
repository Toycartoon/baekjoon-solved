n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = {}
for i in a:
    if i not in s:
        s[i] = 1
    else:
        s[i] += 1

ans = 0
for i in b:
    if i not in s or s[i] < 1:
        ans += 1
    else:
        s[i] -= 1

print(ans)
