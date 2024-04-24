t = int(input())

for _ in range(t):
    a = input().split()
    for i in range(10):
        a[i] = int(a[i])
    a.sort()
    print(a[7])