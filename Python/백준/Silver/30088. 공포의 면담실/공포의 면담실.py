n = int(input())
a = []
for i in range(n):
    s, *l = map(int, input().split())
    a.append(sum(l))


a.sort()
ans = 0
w = 0
for i in a:
    w += i
    ans += w


print(ans)
