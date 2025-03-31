import sys
from datetime import datetime as d

input = sys.stdin.readline

s = input().strip()
n = int(input())

x = set()
for i in range(n):
    x.add(input().strip())

f = True
ans = "I"
if s[:6] not in x:
    f = False

try:
    if not d.strptime("1900-01-01", "%Y-%m-%d") <= d.strptime(s[6:14], "%Y%m%d") <= d.strptime("2011-12-31", "%Y-%m-%d"):
        f = False
except ValueError:
    f = False

if int(s[14:17]) == 0:
    f = False
elif int(s[14:17]) % 2 == 0:
    ans = "F"
elif int(s[14:17]) % 2 == 1:
    ans = "M"

v = 0
for i in range(17):
    v += (int(s[i]) * pow(2, 17-i, 11)) % 11

if s[-1] == "X":
    w = 10
else:
    w = int(s[-1])

if (v + w) % 11 != 1:
    f = False

if not f:
    print("I")
else:
    print(ans)
