n = int(input())
a = list(map(int, input().split()))
l = [0 for _ in range(51)]

for i in a:
    l[i] += 1
    
for i in range(50, -1, -1):
    if l[i] == i:
        print(i)
        exit()

print(-1)