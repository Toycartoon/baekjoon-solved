n = int(input())
d = list(map(int, input().split()))

s = 1
t = 4

ps = 0
pt = 0

r = [0, 0, 0, 0]

def reward():
    global s, t, ps, pt

    if 35 <= ps < 65:
        r[0] += 1
    elif 65 <= ps < 95:
        r[1] += 1
    elif 95 <= ps < 125:
        r[2] += 1
    elif 125 <= ps:
        r[3] += 1

    s = 1
    t = 4
    ps = 0
    pt = 0

for i in d:
    if pt > 240:
        reward()

    if i == 1:
        reward()
        continue
    elif i == 2:
        if s > 1:
            s //= 2
        elif s == 1:
            t += 2
    elif i == 4:
        pt += 56
    elif i == 5:
        if t > 1:
            t -= 1
    elif i == 6:
        if s < 32:
            s *= 2

    ps += s
    pt += t

[print(i) for i in r]
