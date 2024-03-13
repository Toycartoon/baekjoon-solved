n = int(input())

if n == 1:
    print("YES\n1")
    exit()

f = True
for i in range(2, n):
    if (n * (n + 1) // 2) % i == 0:
        f = False
        break

if f:
    print("NO")
    exit()

print("YES")
if n >= 3:
    print("1 3 2 ", end="")
    for i in range(4, n+1):
        print(i, end=" ")
else:
    print(" ".join("132"[:n]))
