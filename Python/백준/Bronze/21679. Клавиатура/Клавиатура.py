n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

for i in p:
    c[i-1] -= 1

for i in c:
    if i < 0:
        print("yes")
    else:
        print("no")
