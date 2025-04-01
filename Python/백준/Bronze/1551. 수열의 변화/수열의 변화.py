n, k = map(int, input().split())
if n == 1:
    print(input())
    exit()
    
a = list(eval(input()))

for _ in range(k):
    b = []
    for i in range(len(a)-1):
        b.append(a[i+1]-a[i])

    a = b

print(*a, sep=",")