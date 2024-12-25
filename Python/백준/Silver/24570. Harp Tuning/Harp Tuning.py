import re

s = input()
numbers = re.findall(r"\d+", s)
etc = re.findall(r"\D+", s)

for i in range(len(etc)):
    if etc[i][-1] == "+":
        print(etc[i][:-1], "tighten", numbers[i])
    elif etc[i][-1] == "-":
        print(etc[i][:-1], "loosen", numbers[i])
