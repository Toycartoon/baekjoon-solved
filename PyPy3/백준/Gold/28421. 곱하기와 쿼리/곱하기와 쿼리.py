import sys

input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    e, x = map(int, input().split())

    if e == 1:
        if x == 0:
            print(int(0 in a and len(a) != 1))
        else:
            f = False
            for i in range(1, int(x ** 0.5) + 1):
                if x % i == 0 and i in a and not f:
                    if (x // i) in a:
                        f = True
                        if x // i == i:
                            if a.count(i) == 1:
                                f = False
            print(int(f))
    else:
        a[x-1] = 0