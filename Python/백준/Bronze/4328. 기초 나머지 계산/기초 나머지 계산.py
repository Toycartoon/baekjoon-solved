import sys

input = sys.stdin.readline

while True:
    b, *pm = map(int, input().split())

    if b == 0:
        break

    mod = int(str(pm[0]), b) % int(str(pm[1]), b)

    ans = ""
    while mod:
        ans += str(mod % b)
        mod //= b


    print(int(str(mod) + ans[::-1]))
