ans = 0
for i in range(int(input())):
    q = []
    for x in input():
        if not q:
            q.append(x)
        else:
            k = q.pop()
            if k != x:
                q.append(k)
                q.append(x)

    if not q:
        ans += 1

print(ans)
