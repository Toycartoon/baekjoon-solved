a = input()
b = input()

lcs = [[0 for _ in range(len(b)+1)] for __ in range(len(a)+1)]

i, j = 0, 0
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            lcs[i][j] = max(lcs[i][j], lcs[i-1][j-1] + 1)
        else:
            lcs[i][j] = max(lcs[i][j], lcs[i-1][j], lcs[i][j-1])

s = ""
x, y = len(a), len(b)
print(lcs[-1][-1])
while len(s) < lcs[-1][-1]:
    if a[x-1] == b[y-1]:
        s += a[x-1]
        x -= 1
        y -= 1
    else:
        if lcs[x-1][y] < lcs[x][y-1]:
            y -= 1
        else:
            x -= 1

print(s[::-1])
