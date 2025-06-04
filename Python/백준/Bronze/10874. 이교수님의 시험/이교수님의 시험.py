n = int(input())
ans = [1, 2, 3, 4, 5] * 2
for i in range(n):
    a = list(map(int, input().split()))
    
    if a == ans:
        print(i + 1)
