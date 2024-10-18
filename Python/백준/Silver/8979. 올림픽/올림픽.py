n, k = map(int, input().split())

l = []
ans = [0 for _ in range(n)]

for i in range(n):
    x, gold, silver, copper = map(int, input().split())
    l.append((x, gold, silver, copper))


for i in range(n):
    a = 0
    for j in range(n):
        if i == j:
            continue

        if l[i][1] < l[j][1]:
            a += 1
        elif l[i][1] == l[j][1] and l[i][2] < l[j][2]:
            a += 1
        elif l[i][1] == l[j][1] and l[i][2] == l[j][2] and l[i][3] < l[j][3]:
            a += 1

    ans[l[i][0]-1] = a


print(ans[k-1] + 1)
