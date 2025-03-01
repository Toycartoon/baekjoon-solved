n = int(input())
g = []

for i in range(n):
    g.append(int(input()))

l, r = 0, 0
lm, rm = 0, 0
for i in range(n):
    if lm < g[i]:
        lm = g[i]
        l += 1

for i in range(n-1, -1, -1):
    if rm < g[i]:
        rm = g[i]
        r += 1

print(l)
print(r)
