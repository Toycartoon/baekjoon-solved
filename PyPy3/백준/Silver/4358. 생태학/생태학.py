t = {}
l = 0
while True:
    try:
        s = input()
        if s not in t:
            t[s] = 1
        else:
            t[s] += 1
        l += 1
    except EOFError:
        break

for i in sorted(t.keys()):
    print("{} {:.4f}".format(i, (t[i] / l) * 100))