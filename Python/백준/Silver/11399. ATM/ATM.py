n = int(input())
p = list(map(int, input().split()))

p.sort()
t = 0
for i in range(1, n + 1):
    t += sum(p[:i])

print(t)