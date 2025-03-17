n = int(input())
m = int(input(), 2)
k = int(input())

if m % (2 ** k) == 0:
    print("YES")
else:
    print("NO")
