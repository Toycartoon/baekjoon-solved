g = ["G...", ".I.T", "..S."]
k = int(input())

for y in range(3):
    for dy in range(k):
        for x in range(4):
            print(g[y][x] * k, end="")
        print()