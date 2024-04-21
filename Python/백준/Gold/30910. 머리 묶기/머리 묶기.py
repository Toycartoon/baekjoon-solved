for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if 3 not in a:
        print(0)
    elif n == 1 and 3 in a:
        print(-1)
    else:
        l = a.index(3)
        r = n - list(reversed(a)).index(3)

        b = 0
        for i in range(l, r):
            b ^= a[i]

        if b != 3 or ((1 in a[:l] or 2 in a[:l]) or (1 in a[r:] or 2 in a[r:])):
            print(1)
        elif b != 3 or (1 in a[l:r] or 2 in a[l:r]) or 0 in a:
            print(2)
        else:
            print(3)