from math import lcm

w = [i for i in range(1000000)]
w[1] = 0

for i in range(2, int(len(w) ** 0.5) + 1):
    if w[i] == 0:
        continue

    for j in range(i * i, len(w), i):
        w[j] = 0

n = int(input())
a = list(map(int, input().split()))

s = []
for i in a:
    if w[i] != 0:
        s.append(i)

print(lcm(*s) if len(s) != 0 else -1)
