s = input()
d = list(map(int, input().split()))

a = 0
h = []
for j in range(1, 7):
    h.append(d.count(j))

for i in range(len(s)):
    if s[i] == "Y":
        if i == 0:
            a = max(a, d.count(1) + 2)
        elif i == 1:
            a = max(a, d.count(2) * 2 + 4)
        elif i == 2:
            a = max(a, d.count(3) * 3 + 6)
        elif i == 3:
            a = max(a, d.count(4) * 4 + 8)
        elif i == 4:
            a = max(a, d.count(5) * 5 + 10)
        elif i == 5:
            a = max(a, d.count(6) * 6 + 12)
        elif i == 6:
            for x in range(5, -1, -1):
                if h[x] >= 2:
                    a = max(a, (x + 1) * 4)
        elif i == 7:
            if h.count(0) == 4:
                if h.index(2) + 1 >= h.index(1) + 1:
                    a = max(a, (h.index(2) + 1) * 3 + (h.index(1) + 1) * 2)
                else:
                    a = max(a, (h.index(2) + 1) * 2 + (h.index(1) + 1) * 3)
            elif h.count(0) == 5:
                if h.index(3) + 1 == 6:
                    a = max(a, (h.index(3) + 1) * 3 + 10)
                else:
                    a = max(a, (h.index(3) + 1) * 3 + 12)
        elif i == 8:
            if h.count(1) == 3 and h[5] == 0:
                a = max(a, 30)
        elif i == 9:
            if h.count(1) == 3 and h[0] == 0:
                a = max(a, 30)
        elif i == 10:
            if 3 in h:
                a = max(a, 50)
        else:
            a = max(a, sum(d) + 12)

print(a)