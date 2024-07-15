n = int(input())
c = [set(), set()]

ans = 0
for i in range(n):
    a, b = map(int, input().split())

    if b == 1:
        if a in c[0]:
            c[0].remove(a)
            ans += 1
    elif b == 0:
        if a in c[1]:
            c[1].remove(a)
            ans += 1

    c[b].add(a)

print(ans)
