n = int(input())
g = [[*input()] for _ in range(2)]

ans = 0
for i in range(n):
    if g[0][i] == g[1][i] == "C":
        ans += 1

print(ans)
