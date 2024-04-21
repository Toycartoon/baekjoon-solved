w = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0}
c = set()

for _ in range(int(input())):
    s = input()
    for i in range(len(s)):
        try:
            w[s[i]] += 10 ** (len(s) - (1 + i))
        except KeyError:
            w[s[i]] = 10 ** (len(s) - (1 + i))
        c.add(s[0])

v = list(w.values())
v.sort(reverse=True)

if v.count(0) == 0:
    temp = {"A", "B", "C", "D","E", "F", "G", "H", "I", "J"}
    for key in w:
        if key in c:
            temp.remove(key)
    if len(temp) == 0:
        v[v.index(w[temp.pop()])] = 0
    else:
        m = 10 ** 13
        for i in temp:
            a = v[v.index(w[i])]
            if a < m:
                m = a

        v[v.index(m)] = 0


v.sort(reverse=True)
for i in range(1, len(v) + 1):
    v[i - 1] = v[i - 1] * (10 - i)

print(sum(v))