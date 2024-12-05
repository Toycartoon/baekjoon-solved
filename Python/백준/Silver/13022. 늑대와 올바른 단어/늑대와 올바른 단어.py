s = input()

q = [*s]

f = True
p = "flow"
while q:
    c = [0 for _ in range(4)]
    for i in range(4):
        x = 0
        try:
            while q[-1] == p[i]:
                x += 1
                q.pop()
        except IndexError:
            pass

        c[i] = x

    if c.count(c[0]) != len(c):
        f = False
        break


print(int(f))
