n = int(input())
a = list(map(int, input().split()))

s = sorted(a)
ans = []

for i in a:
    x = s.index(i)
    ans.append(x)
    s[x] = -1

print(*ans)
