h = int(input())
m = int(input())

for t in range(1, m+1):
    if -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t <= 0:
        print("The balloon first touches ground at hour:", t)
        exit()

print("The balloon does not touch ground in the given time.")
