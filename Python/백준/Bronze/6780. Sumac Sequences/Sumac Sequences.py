t = []
for i in range(2):
    t.append(int(input()))

while t[-2] >= t[-1]:
    t.append(t[-2] - t[-1])

print(len(t))
