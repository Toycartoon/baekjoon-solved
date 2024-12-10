w = [[1, 3], [6, 8], [2, 5]]
l = []
for _ in range(3):
    l.append(int(input()))

f = True
for i in range(3):
    if l[i] not in w[i]:
        f = False
        break

        
if f:
    print("JAH")
else:
    print("EI")
