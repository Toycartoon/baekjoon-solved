import sys

input = sys.stdin.readline

s, t = 0, 0
for i in range(int(input())):
    a = input().strip().upper()

    s += a.count("S")
    t += a.count("T")

if s >= t:
    print("French")
else:
    print("English")
