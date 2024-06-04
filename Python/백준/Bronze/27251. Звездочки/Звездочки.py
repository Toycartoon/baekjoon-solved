n = int(input())
for k in range(1, n+1):
    if k ** 2 > 100:
        print("*" * 100 + "...")
    else:
        print("*" * (k ** 2))
