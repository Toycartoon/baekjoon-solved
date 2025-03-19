from math import isqrt

a, b = map(int, input().split())

ans = set()
ans.add(-a + isqrt(a ** 2 - b))
ans.add(-a - isqrt(a ** 2 - b))

print(*sorted(list(ans)))
