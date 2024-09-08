from math import comb

while True:
    n, k = map(int, input().split())
    
    if n == k == 0:
        break
        
    print(comb(n, k))
    