n = int(input())
s = input()
a = ""
for i in s:
    if i not in "JAV":
        a += i

print(a if a else "nojava")