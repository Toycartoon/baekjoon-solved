n = int(input())
a = list(map(int, input().split()))

ans = 0
while a.count(0) != n:
    a.sort(reverse=True)
    try:
        a[0] -= 1
        if a[1] != 0:
            a[1] -= 1
    except IndexError:
        pass
    ans += 1

if ans > 1440:
    print(-1)
else:
    print(ans)