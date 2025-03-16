import sys

input = sys.stdin.readline

j = int(input())
a = int(input())
v = [True for _ in range(j+1)]
x = [-1]

ans = 0
for i in range(j):
    x.append(input().strip())

w = {"S": "SML", "M": 'ML', "L": "L"}
for i in range(a):
    s, n = input().split()

    if v[int(n)] and x[int(n)] in w[s]:
        ans += 1
        v[int(n)] = False

print(ans)
