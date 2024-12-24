from math import trunc

r, k, m = map(int, input().split())

i = 1
while True:
    if i * k <= m:
        r = trunc(r / 2)
        
        if r == 0:
            print(0)
            break
            
        i += 1
    else:
        print(r)
        break
