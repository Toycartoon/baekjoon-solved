k = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']

for t in range(int(input())):
    s = input()

    print(f"Case #{t+1}", end=": ")
    for i in s:
        if i.isalpha():
            print(k[ord(i)-97], end="")
        else:
            print(i, end="")

    print()
