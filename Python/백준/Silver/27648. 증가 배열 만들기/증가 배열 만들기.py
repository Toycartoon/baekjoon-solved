n, m, k = map(int, input().split())

if n + m - 1 > k:
    print("NO")
else:
    print("YES")
    for i in range(n):
        for j in range(1, m+1):
            print(i + j, end=" ")
        print()
