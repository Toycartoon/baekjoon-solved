from math import factorial as f

for _ in range(int(input())):
    n, m = map(int, input().split())

    print(f(m) // (f(n) * f(m - n)))