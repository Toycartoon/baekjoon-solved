import sys

n = int(input())
a = list(map(int, input().split()))
d = []

sys.setrecursionlimit(10 ** 6)


def check(i):
    if i in d:
        return True
    return False


for i in a:
    if i != 0 and i not in d:
        d.append(i)
    elif i in d:
        while check(i):
            d.remove(i)
            i = i * 2
        d.append(i)

print(max(d))