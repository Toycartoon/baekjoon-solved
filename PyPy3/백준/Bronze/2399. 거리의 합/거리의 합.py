n = int(input())
l = list(map(int, input().split()))

a = 0
for i in range(n):
    for j in range(n):
        a += abs(l[i] - l[j])

print(a)