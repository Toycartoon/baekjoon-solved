s = input()
a = []
n = []
for i in s:
    if i.isalpha():
        a.append(i)
    elif i.isnumeric():
        n.append(i)

a.sort()
n.sort(reverse=True)
for i in range(3):
    print(a[i], end="")
    print(n[i], end="")
