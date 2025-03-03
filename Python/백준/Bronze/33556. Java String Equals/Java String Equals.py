a = input()
b = input()

if a == "null":
    print("NullPointerException\n" * 2)
    exit()
elif b == "null":
    print("false\n" * 2)
else:
    print(str(a == b).lower())
    print(str(a.lower() == b.lower()).lower())
