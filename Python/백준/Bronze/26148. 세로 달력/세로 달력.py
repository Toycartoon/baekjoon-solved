n = int(input())
d = int(input())

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(30)
else:
    print(29)
