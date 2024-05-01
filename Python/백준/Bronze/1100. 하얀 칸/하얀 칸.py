g = [[*input()] for _ in range(8)]

ans = 0
for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        if g[i][j] == "F":
            ans += 1
    for j in range(1, 8, 2):
        if g[i+1][j] == "F":
            ans += 1

print(ans)
