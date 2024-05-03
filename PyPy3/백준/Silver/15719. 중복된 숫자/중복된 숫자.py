import sys

input = sys.stdin.readline

n = int(input())
l = input()

s = (n - 1) * n // 2
x = ""
a = 0
for i in l:
    if i == " ":
        a += int(x)
        x = ""
    else:
        x += i
a += int(x)
print(abs(a - s))