k, n = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))

l = -1
r = 2 ** 31
while l + 1 < r:
    mid = (l + r) // 2

    a = 0
    for i in line:
        a += i // mid

    if a >= n:
        l = mid
    else:
        r = mid

print(l)
