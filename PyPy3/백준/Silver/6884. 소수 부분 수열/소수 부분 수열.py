import sys
from math import isqrt

input = sys.stdin.readline

def prime(n):
    if n < 2:
        return False

    for i in range(2, isqrt(n) + 1):
        if not p[i]:
            continue

        if n % i == 0:
            return False
    return True

p = [True for _ in range(10001)]
p[0] = False
p[1] = False

for i in range(2, isqrt(len(p)) + 1):
    if not p[i]:
        continue
    for j in range(i * 2, len(p), i):
        p[j] = False

for t in range(int(input())):
    ps = []
    x = 0

    n, *a = map(int, input().split())
    for i in range(n):
        ps.append(x)
        x += a[i]
    ps.append(x)

    f = True
    for i in range(2, n+1):
        if not f:
            break

        for j in range(i, len(ps)):
            if prime(ps[j]-ps[j-i]):
                print(f"Shortest primed subsequence is length {i}: ", end="")
                print(*a[j-i:j])
                f = False
                break

    if f:
        print("This sequence is anti-primed.")
