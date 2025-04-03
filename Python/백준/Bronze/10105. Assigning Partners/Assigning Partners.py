n = int(input())
a = input().split()
b = input().split()

w = {}
for i in range(n):
    w[a[i]] = b[i]

f = True
for i in w:
    if i != w[w[i]] or i == w[i]:
        f = False

if f:
    print("good")
else:
    print("bad")
