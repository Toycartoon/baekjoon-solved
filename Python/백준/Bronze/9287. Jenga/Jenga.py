import sys

input = sys.stdin.readline

for t in range(int(input())):
    f = True
    for i in range(int(input())):
        s = input().strip()
        if s == "100" or s == "001" or s == "000":
            f = False

    print(f"Case {t+1}: {'Standing' if f else 'Fallen'}")
