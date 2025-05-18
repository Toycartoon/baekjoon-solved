n, k = map(int, input().split())
r = []
for i in range(k):
    r.append(float(input()))

print(sum([-3 * (n-k), *r]) / n, sum([3 * (n-k), *r]) / n)
