p = []
for i in range(3):
    p.append(tuple(input().split()))

p.sort(key=lambda x: x[1])
print("".join([str(int(j[1]) % 100) for j in p]))
p.sort(key=lambda x: int(x[0]), reverse=True)
print("".join([i[2][0] for i in p]))