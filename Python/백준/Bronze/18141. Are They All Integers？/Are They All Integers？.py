n = int(input())
a = list(map(int, input().split()))

f = True
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k:
                continue

            if (a[i] - a[j]) % a[k] != 0:
                f = False
                break

if f:
    print("yes")
else:
    print("no")
