x = int(input())
k = []
for i in range(1, int((x + 1) ** 0.5)+1):
    if (x + 1) % i == 0:
        k.append(i)
        if i < (x + 1) // i:
            k.append((x + 1) // i)

k.sort()
k.pop()
print(*k)
