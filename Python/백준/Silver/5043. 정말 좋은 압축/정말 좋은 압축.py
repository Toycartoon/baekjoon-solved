n, b = map(int, input().split())

a = 0
for i in range(b+1):
    a += pow(2, i)

if a >= n:
    print("yes")
else:
    print("no")
