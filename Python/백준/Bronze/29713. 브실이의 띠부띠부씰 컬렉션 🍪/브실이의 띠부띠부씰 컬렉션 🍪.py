w = {"B": 0, "R": 0, "O": 0, "N": 0, "Z": 0, "E": 0, "S": 0, "I": 0, "L": 0, "V": 0}
n = int(input())
s = input()
for i in s:
    if i in w:
        w[i] += 1

w["E"] //= 2
w["R"] //= 2
print(min(w.values()))
