n, m, k, a, b, c = map(int, input().split())
ans = [n * a, m * b, k * c]

x = max(ans)
l = ["Joffrey", "Robb", "Stannis"]
for i in range(3):
    if ans[i] == x:
        print(l[i], end=" ")
