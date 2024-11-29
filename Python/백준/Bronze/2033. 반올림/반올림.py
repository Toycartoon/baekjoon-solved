x = list(map(int, [*input().strip()]))

if len(x) == 1:
    print(x[0])
    exit()

for i in range(len(x)-2, -1, -1):
    if x[i+1] >= 5:
        x[i] += 1
    x[i+1] = 0

for i in x:
    print(i, end="")
