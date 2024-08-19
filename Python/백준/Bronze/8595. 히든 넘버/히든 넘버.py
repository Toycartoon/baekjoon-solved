n = int(input())
s = input()

ans = 0
x = "0"
for i in s:
    if i.isnumeric():
        x += i
    else:
        ans += int(x)
        x = "0"


ans += int(x)
print(ans)
