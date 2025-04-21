n = int(input())
ans = [["*" for _ in range(1 + (4 * (n-1)))] for __ in range(1 + (4 * (n-1)))]

t = 1
for i in range(2 * (n-1)):
    if t % 2 == 1:
        q = " "
    elif t % 2 == 0:
        q = "*"

    for y in range(t, len(ans)-t):
        for x in range(t, len(ans)-t):
            ans[y][x] = q

    t += 1

for v in ans:
    print("".join(v))
