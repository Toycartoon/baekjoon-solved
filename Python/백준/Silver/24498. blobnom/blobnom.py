n = int(input())
a = list(map(int, input().split()))

t = [a[0], a[n - 1]]
for i in range(1, n - 1):
    t.append(a[i] + min(a[i - 1], a[i + 1]))

print(max(t))