s = input()

ans = ""

r = True
x = ""
for i in s:
    if i == "<":
        if x != "":
            ans += x[::-1]
        x = ""
        r = False
    elif i == ">":
        r = True
        x += i
        ans += x
        x = ""
        continue
    elif i == " ":
        if r:
            ans += x[::-1] + " "
            x = ""
            continue

    x += i


if r:
    ans += x[::-1]
else:
    ans += x

print(ans)
