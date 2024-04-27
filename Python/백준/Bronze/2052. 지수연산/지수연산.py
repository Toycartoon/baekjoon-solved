n = int(input())
n = 2 ** n
print("0.", end="")
a = 1
while True:
    a = (a % n) * 10
    if a == 0:
        break
    print(a // n, end="")