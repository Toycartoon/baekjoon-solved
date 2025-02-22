n, m = map(int, input().split())
g = [i+1 for i in range(n)]

for x in range(m):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    k -= 1
    g = g[:i] + g[k:j+1] + g[i:k] + g[j+1:]


print(*g)
