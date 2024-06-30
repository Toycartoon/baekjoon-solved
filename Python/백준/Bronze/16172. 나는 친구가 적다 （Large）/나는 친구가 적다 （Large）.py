s = input()
k = input()

ns = ""
for i in s:
    if i.isalpha():
        ns += i

print(int(k in ns))
