n = input().split()

for _ in range(len(n)):
    n[_] = int(n[_])

n.sort()

for _ in range(len(n)):
    n[_] = str(n[_])

print(" ".join(n))