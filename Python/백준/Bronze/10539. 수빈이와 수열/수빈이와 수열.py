n = int(input())
b = list(map(int, input().split()))

a = []
s = 0
for i in range(n):
    a.append((b[i] * (i + 1)) - s)
    s += a[-1]

print(*a)
