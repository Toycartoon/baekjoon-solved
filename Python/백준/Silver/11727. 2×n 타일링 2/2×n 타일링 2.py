import sys

sys.setrecursionlimit(10 ** 6)

m = {1: 1, 2: 3}
def c(i):
    if i in m:
        return m[i]
    m[i] = c(i - 1) + c(i - 2) * 2
    return m[i]

print(c(int(input())) % 10007)