for t in range(int(input())):
    a, b = input().split()
    print(int(str(int(a[::-1]) + int(b[::-1]))[::-1]))
