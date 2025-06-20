n, k = map(int, input().split())

if n == k:
    print("Impossible")
    exit()
elif n == k+1:
    [print(i, end=" ") for i in range(1, n+1)]
    exit()

print(n, end=" ")
for i in range(k):
    print(i+2, end=" ")

print(1, end=" ")
for i in range(k+1, n-1):
    print(i+1, end=" ")
