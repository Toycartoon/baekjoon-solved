s = input()
b = ""
ans = 0

for i in s:
    if i != b:
        ans += 10
        b = i
    else:
        ans += 5

print(ans)
