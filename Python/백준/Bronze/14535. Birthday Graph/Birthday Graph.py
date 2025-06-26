import sys

input = sys.stdin.readline

m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
t = 1
while True:
    n = int(input())
    a = [0 for _ in range(12)]

    if n == 0:
        break

    for i in range(n):
        date, month, year = map(int, input().split())
        a[month - 1] += 1

    print(f"Case #{t}:")
    for i in range(12):
        print(f"{m[i]}:{'*' * a[i]}")

    t += 1
