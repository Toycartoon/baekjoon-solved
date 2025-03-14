import sys

input = sys.stdin.readline

m = input().strip()
ans = "No Jam"
ap = 0
for n in range(int(input())):
    w, g = input().strip().split()

    if len(w) < len(m):
        continue

    x = 0
    for i in range(len(w)):
        if x == len(m):
            break

        if w[i] == m[x]:
            x += 1

    if x != len(m):
        continue

    v = int(g) / (len(w) - len(m))
    if v > ap:
        ap = v
        ans = w

print(ans)
