n = input().split()
p = input()

for _ in range(len(n)):
    n[_] = int(n[_])
n.sort()
abc = ""
for i in p:
    if i == "A":
        abc += str(n[0])
    elif i == "B":
        abc += str(n[1])
    else:
        abc += str(n[2])
    abc += " "

print(abc)