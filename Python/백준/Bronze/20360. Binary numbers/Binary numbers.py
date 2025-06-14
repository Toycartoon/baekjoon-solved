n = int(input())
for i in range(len(bin(n))):
    if bin(n)[::-1][i] == "1":
        print(i, end=" ")
