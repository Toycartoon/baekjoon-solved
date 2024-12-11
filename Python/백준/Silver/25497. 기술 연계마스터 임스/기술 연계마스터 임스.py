s, l = 0, 0
ans = 0
n = int(input())
for i in input():
    if i.isnumeric():
        ans += 1
    elif i == "S":
        s += 1
    elif i == "L":
        l += 1
    elif i == "R":
        if l > 0:
            l -= 1
            ans += 1
        else:
            break
    elif i == "K":
        if s > 0:
            s -= 1
            ans += 1
        else:
            break


print(ans)
