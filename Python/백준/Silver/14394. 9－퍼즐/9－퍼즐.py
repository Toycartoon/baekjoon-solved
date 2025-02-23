w = {"B": 0, "G": 0, "Y": 0, "R": 0}

s = input()
for i in s:
    if i == "*":
        continue
    w[i] += 1

ans = 0
for i in input():
    if i == "*":
        continue

    if w[i] == 0:
        ans += 1
    else:
        w[i] -= 1


print(ans)
