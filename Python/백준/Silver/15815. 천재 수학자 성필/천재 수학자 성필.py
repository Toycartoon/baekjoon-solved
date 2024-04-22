s = []
x = input()

for i in x:
    if i == "+":
        a = s.pop()
        b = s.pop()
        s.append(b + a)
    elif i == "-":
        a = s.pop()
        b = s.pop()
        s.append(b - a)
    elif i == "*":
        a = s.pop()
        b = s.pop()
        s.append(b * a)
    elif i == "/":
        a = s.pop()
        b = s.pop()
        s.append(b // a)
    else:
        s.append(int(i))

print(s[0])