for t in range(int(input())):
    a, b = map(float, input().split())

    if abs((a / b) - 1.61803399) <= 0.01:
        print("golden")
    else:
        print("not")
