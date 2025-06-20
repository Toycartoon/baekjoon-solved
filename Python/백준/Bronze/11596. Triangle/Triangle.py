a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
if a == sorted(b) and a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
    print("YES")
else:
    print("NO")
