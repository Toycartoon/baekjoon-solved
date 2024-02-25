import sys

x = int(sys.stdin.readline())

d = 1
m = 1
f = True
for i in range(1, x):
    if f:
        d += 1
        if m != 1:
            m -= 1
        else:
            f = not f
    else:
        m += 1
        if d != 1:
            d -= 1
        else:
            f = not f

sys.stdout.write(f"{m}/{d}")