for t in range(int(input())):
    print(f"Case {t+1}:")
    n = int(input())

    for i in range(n):
        s = int(input())
        if s + 1 < 7:
            print(s+1)
