a = 0
s = ""
while True:
    try:
        s += input()
    except EOFError:
        s = s.split(",")
        for i in s:
            a += int(i)
        break

print(a)