import sys

input = sys.stdin.readline

for _ in range(int(input())):
    t, *n = map(int, input().split())
    w = {}
    v = t // 2 + 1
    f = False

    for i in n:
        if i not in w:
            w[i] = 1
        else:
            w[i] += 1

        if w[i] >= v:
            print(i)
            f = True
            break

    if not f:
        print("SYJKGW")
