t = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    l = []
    arr = [0] * n
    for i in range(n):
        l.append(input())
    
    for i in range(2 * n - 1):
        x, a = input().split()
        arr[int(x)-1] += 1
    
    for i in range(len(arr)):
        if arr[i] != 2:
            print(t, l[i])
            break
    
    t += 1