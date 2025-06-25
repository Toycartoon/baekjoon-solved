k = int(input())
n = int(input())

for i in range(n-1):
    print(i+1)
    k -= i+1

print(k)
