l = []
[l.append(int(input())) for i in range(9)]

print(max(l))
print(l.index(max(l)) + 1)