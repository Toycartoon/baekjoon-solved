n = int(input())
a = list(map(int, input().split()))

w = {0: 2, 1: 1, 2: 0.5, 4: 0.25, 8: 0.125, 16: 0.0625}
ans = 0
for i in a:
    ans += w[i]

print(ans)
