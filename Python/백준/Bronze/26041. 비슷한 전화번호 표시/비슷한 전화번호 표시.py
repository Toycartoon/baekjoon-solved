a = input().split()
b = input()

ans = 0
for i in a:
    if i.startswith(b) and i != b:
        ans += 1

print(ans)
