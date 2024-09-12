import sys

sys.setrecursionlimit(10 ** 6)

s = input()
t = input()


def f(x):
    if x == s:
        print(1)
        sys.exit()
    if len(x) == 0:
        return

    if x[-1] == "A":
        f(x[:-1])
    if x[0] == "B":
        f(x[1:][::-1])


f(t)
print(0)
