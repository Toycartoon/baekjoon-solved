a, b, c, d = map(int, input().split())
l = list(map(int, input().split()))

ans = []
for i in l:
    x = 0
    if 0 < i % (a + b) <= a:
        x += 1
    if 0 < i % (c + d) <= c:
        x += 1

    ans.append(x)

for i in ans:
    print(i)
