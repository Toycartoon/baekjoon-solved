n = int(input())
h = [0 for _ in range(n)]

h[-1] = str(n)
f = True

i = n - 1
fp = 0
bp = len(h) - 2
while i > 0:
    if f:
        for j in range(fp, fp + 2):
            h[j] = str(i)
            i -= 1
            fp += 1
            if i <= 0:
                break
    else:
        for j in range(bp, bp - 2, -1):
            h[j] = str(i)
            i -= 1
            bp -= 1
            if i <= 0:
                break

    f = not f

print(" ".join(h))
