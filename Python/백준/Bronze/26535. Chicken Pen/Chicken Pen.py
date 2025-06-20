a = int(input())

n = 1
while True:
    if (n - 2 if n - 2 > 0 else 0) ** 2 >= a:
        break
    n += 1

print("x" * n)
for i in range(n-2):
    print("x" + "." * (n-2) + "x")
print("x" * n)
