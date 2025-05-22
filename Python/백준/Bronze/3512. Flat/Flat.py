n, c = map(int, input().split())
bed = 0
bal = 0

s = 0
for i in range(n):
    a, t = input().split()
    s += int(a)

    if t == "bedroom":
        bed += int(a)
    elif t == "balcony":
        bal += int(a)

print(s)
print(bed)
print((s - (bal / 2)) * c)
