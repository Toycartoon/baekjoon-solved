from math import factorial as f

n, m, k = map(int, input().split())

if k != 0:
    y = (k - 1) // m
    x = m - 1 if k % m == 0 else k % m - 1

    print((f(x+y) // (f(x) * f(y))) * (f(n-y+m-x-2) // (f(m-x-1) * f(n-y-1))))
else:
    print(f(n+m-2) // (f(n-1) * f(m-1)))
