n = int(input())
a = list(map(int, input().split()))
x = [False for _ in range(n)]

for i in a:
    x[i-1] = not x[i-1]

for i in range(n):
    if x[i]:
        print(i+1)
        break
