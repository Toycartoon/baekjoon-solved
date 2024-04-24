for _ in range(int(input())):
    s = input().split()
    print(" ".join((lambda x: x[::-1])(s[i]) for i in range(len(s))))