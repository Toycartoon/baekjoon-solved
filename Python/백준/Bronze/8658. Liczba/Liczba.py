n = int(input())
mn, mx = 0, 0
for i in range(1, n+1):
    if n % i != 0:
        mn = i
        break

for i in range(n, 1, -1):
    if n % i != 0:
        mx = i
        break

print(mn, mx)
