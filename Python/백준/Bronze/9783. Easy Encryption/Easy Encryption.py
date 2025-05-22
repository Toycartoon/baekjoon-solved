s = input()
for i in s:
    if i.isupper():
        print(ord(i)-38, end="")
    elif i.islower():
        print(str(ord(i)-96).zfill(2), end="")
    elif i.isdigit():
        print(f"#{i}", end="")
    else:
        print(i, end="")
