n, k = map(int, input().split())

if n == 2 and k == 1:
    print("1 2")
elif n > k or n >= 2:
    print(-1)
else:
    print("1 " * (n * k))
