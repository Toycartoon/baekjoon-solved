n = int(input())
ans = 0
for i in range(n):
    t = list(map(int, input().split()))

    if t[0] == -1:
        continue
    elif t[1] == -1:
        if t[2] != -1:
            continue
        else:
            ans += 1
    elif t[2] == -1:
        if t[0] <= t[1]:
            ans += 1
        else:
            continue
    else:
        if sorted(t) == t:
            ans += 1

print(ans)
