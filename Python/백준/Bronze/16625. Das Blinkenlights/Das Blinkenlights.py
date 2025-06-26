p, q, s = map(int, input().split())

f = False
for i in range(1, s+1):
    if i % p == 0 and i % q == 0:
        f = True
        break

print("yes" if f else "no")