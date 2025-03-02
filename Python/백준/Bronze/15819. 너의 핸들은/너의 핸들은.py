g = []
n, l = map(int, input().split())

for i in range(n):
    g.append(input())
    
g.sort()
print(g[l-1])