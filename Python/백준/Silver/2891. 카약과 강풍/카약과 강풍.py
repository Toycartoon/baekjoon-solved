n, s, r = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

ans = s
for i in range(s):
    if a[i] in l:
        l.remove(a[i])
        a[i] = -1
        ans -= 1

for i in a:
    f = False
    for x in l:
        if abs(i - x) <= 1:
            l.remove(x)
            f = True
            break

    if f:
        ans -= 1

print(ans)
