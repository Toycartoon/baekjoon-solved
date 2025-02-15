n = int(input())

print("int a;")
for i in range(1, n + 1):
    print(f"int {'*' * i}ptr", end="")
    if i - 1 == 0:
        print(" = &a;")
    elif i - 1 == 1:
        print("2 = &ptr;")
    else:
        print(f"{i if i - 1 > 1 else ''} = &{'ptr'+ str(i - 1)};")