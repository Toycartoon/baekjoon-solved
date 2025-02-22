from math import comb

l = int(input())
s = list(map(int, input().split()))
n = int(input())

if n in s:
    print(0)
    exit()

s.sort()
if n < s[0]:
    print(comb(s[0]-1, 2) - comb(n-1, 2) - comb(s[0]-n-1, 2))
    exit()

for i in range(1, l):
    if s[i-1] < n < s[i]:
        print(comb(s[i]-s[i-1]-1, 2) - comb(n-s[i-1]-1, 2) - comb(s[i]-n-1, 2))
        break
