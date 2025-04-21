n = int(input())
m = int(input())
a = list(map(int, input().split()))

l = [False for _ in range(100001)]
for i in a:
    l[i] = True

ans = 0
for i in a:
    if 0 <= m-i < len(l) and l[m-i]:
        ans += 1

print(ans // 2)
