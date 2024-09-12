g = [True] * 5000001
g[0] = False
g[1] = False
for i in range(2, int(5000001 ** 0.5)):
    if g[i]:
        for j in range(i * i, 5000001, i):
            g[j] = False


for t in range(int(input())):
    ans = 0
    
    n = int(input())
    for i in range(1, n // 2 + 1):
        if g[i] and g[n-i]:
            ans += 1

    print(ans)
