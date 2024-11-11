from math import log2


n = int(input())
l = []
x = 1
for i in range(1, int(log2(n))):
    print(f"? {x}", flush=True)
    l.append(int(input()))
    x += n // int(log2(n))


print(f"? {n}", flush=True)
l.append(int(input()))

u, d = 0, 0
for i in range(len(l)-1):
    if l[i] > l[i+1]:
        d += 1
    elif l[i] < l[i+1]:
        u += 1


if u > d:
    print("! 1", flush=True)
elif u < d:
    print("! -1", flush=True)
else:
    print("! 0", flush=True)