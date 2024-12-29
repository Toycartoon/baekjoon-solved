x, y = input().split()

if x.isdigit() and y.isdigit():
    print(int(x) - int(y))
else:
    print("NaN")
