a, b = map(int, input().split())
m = int(input())
n = list(map(int, input().split()))[::-1]

d = 0
for i in range(m):
    d += n[i] * (a ** i)

ans = []
while d // b:
    ans.append(d % b)
    d //= b

ans.append(d)
print(*ans[::-1])
