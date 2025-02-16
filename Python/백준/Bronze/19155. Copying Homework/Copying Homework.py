n = int(input())
a = list(map(int, input().split()))

for i in a:
    print(n+1-i, end=" ")