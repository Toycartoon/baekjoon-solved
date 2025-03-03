import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b = input().strip().split()

    a = a[::-1]
    b = b[::-1]

    ans = ""
    for i in range(min(len(a), len(b))):
        ans = str(int(a[i]) * int(b[i])) + ans

    a = a[::-1]
    b = b[::-1]
    if len(a) < len(b):
        ans = b[:len(b)-len(a)] + ans
    else:
        ans = a[:len(a)-len(b)] + ans

    print(int(int(ans) == int(a) * int(b)))
