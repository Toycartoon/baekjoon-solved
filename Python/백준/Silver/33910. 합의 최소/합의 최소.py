n = int(input())
a = list(map(int, input().split()))

ans = 0
ad = a[-1]
for i in a[::-1]:
    ad = min(ad, i)
    ans += ad

print(ans)
