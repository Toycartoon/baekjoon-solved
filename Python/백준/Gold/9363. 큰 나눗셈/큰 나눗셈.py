import sys, math, functools

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    an = functools.reduce(lambda x, y: x * y, a)
    bn = functools.reduce(lambda x, y: x * y, b)

    g = math.gcd(an, bn)

    print(f"Case #{t + 1}: {an // g} / {bn // g}")
