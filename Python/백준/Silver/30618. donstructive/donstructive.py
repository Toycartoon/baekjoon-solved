n = int(input())
a, b = [], []
for i in range(1, n+1):
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)

print(*(a + b[::-1]))
