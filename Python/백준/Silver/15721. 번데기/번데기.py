a = int(input())
t = int(input())
s = int(input())

ans = 0
g = [0, 1, 0, 1, 0, 0, 1, 1]

idx = 0
x = 0
while x < t:
    ans += 1
    if idx == len(g):
        g.insert(4, 0)
        g.append(1)

        if g[0] == s:
            x += 1
        idx = 1
        continue

    if g[idx] == s:
        x += 1

    idx += 1


print((ans-1) % a)
