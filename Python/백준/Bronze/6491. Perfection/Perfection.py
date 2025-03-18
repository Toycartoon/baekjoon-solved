import sys

input = sys.stdin.readline

n = []
while True:
    n.extend(list(map(int, input().split())))
    if n[-1] == 0:
        break

for i in n:
    if i == 0:
        break

    a = 0
    for x in range(i // 2, 0, -1):
        if i % x == 0:
            a += x

    if a == i:
        print(i, "PERFECT")
    elif a < i:
        print(i, "DEFICIENT")
    else:
        print(i, "ABUNDANT")
