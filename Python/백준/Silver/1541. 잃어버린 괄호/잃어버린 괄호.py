s = input()
p = []
i = ""
for x in s:
    if x == "+" or x == "-":
        if i[0] == "+" or i[0] == "-":
            p.append(i[0] + i[1:].lstrip('0'))
        else:
            p.append(i.lstrip('0'))
        i = ""
    i += x

if i[0] == "+" or i[0] == "-":
    p.append(i[0] + i[1:].lstrip('0'))
else:
    p.append(i.lstrip('0'))

m = False
for v in range(len(p)):
    if p[v][0] == "-":
        m = True
    elif p[v][0] == "+" and m:
        p[v] = "-" + p[v][1:]

print(eval("".join(p)))
