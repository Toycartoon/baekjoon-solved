a = []
b = 42
mod = []

for i in range(10):
    a.append(int(input()))

for j in range(len(a)):
    flag = True
    for k in range(len(mod)):
        if a[j] % b == mod[k]:
            flag = False
    if flag:
        mod.append(a[j] % b)

print(len(mod))