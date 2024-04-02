from math import ceil

n = input()
num = [0 for _ in range(9)]

for i in n:
    if i == "9":
        num[6] += 1
    else:
        num[int(i)] += 1

num[6] = ceil(num[6] / 2)
print(max(num))
