l, r, a = map(int, input().split())

if l == r:
    print(l + r + a // 2 * 2)
else:
    if min(l, r) + a < max(l, r):
        print((min(l, r) + a) * 2)
    else:
        print(max(l, r) * 2 + (a - (max(l, r) - min(l, r))) // 2 * 2)
