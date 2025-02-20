n = int(input())
a = list(map(int, input().split()))

ans = 0
c = [0, 0, 0, 0]
for i in a:
    c[i] += 1

x = min(c[0], c[3])
ans += 3 * x
c[0] -= x
c[3] -= x

x = min(c[1], c[2])
ans += 3 * x
c[1] -= x
c[2] -= x

x = min(c[0], c[2])
ans += 2 * x
c[0] -= x
c[2] -= x

x = min(c[1], c[3])
ans += 2 * x
c[1] -= x
c[3] -= x

ans += min(c[0], c[1])
ans += min(c[2], c[3])

print(ans)
