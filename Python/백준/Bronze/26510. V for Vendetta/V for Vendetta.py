n = list(map(int, input().split()))

for i in n:
    for x in range(i-1):
        print(" " * x + "*" + " " * (2 * (i-x-1) - 1) + "*")
    print(" " * (i-1) + "*")
