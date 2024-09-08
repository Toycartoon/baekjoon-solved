n, d = map(int, input().split())
a = 0
for i in range(1, n+1):
    a += str(i).count(f"{d}")

print(a)
