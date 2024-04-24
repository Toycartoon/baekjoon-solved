n = int(input())
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
    
m = max(l)
for i in range(len(l)):
    l[i] = (l[i] / m) * 100

total = 0
for s in l:
    total += s

print(total / len(l))