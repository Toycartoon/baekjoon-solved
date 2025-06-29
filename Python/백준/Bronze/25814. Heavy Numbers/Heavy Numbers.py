a, b = input().split()
a = len(a) * sum(list(map(int, [*a])))
b = len(b) * sum(list(map(int, [*b])))

if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)
