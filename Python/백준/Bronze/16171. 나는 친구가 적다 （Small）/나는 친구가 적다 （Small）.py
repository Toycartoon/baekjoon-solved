s = input()
k = input()

for i in s:
    try:
        int(i)
        s = s.replace(i, "")
    except ValueError:
        pass

if k in s:
    print(1)
else:
    print(0)