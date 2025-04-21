n = int(input())
c = list(map(int, input().split()))

op = []
for i in range(n):
    for j in range(1, n):
        if i == j:
            continue

        if c[j-1] > c[j]:
            c[j-1], c[j] = c[j], c[j-1]
            op.append((j, j+1))

print(len(op))
for v in op:
    print(*v)
