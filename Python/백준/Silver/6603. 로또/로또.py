from itertools import combinations as c

while True:
    k, *s = input().split()
    
    if k == "0":
        break
    
    comb = c(s, 6)
    while True:
        try:
            print(" ".join(next(comb)))
        except StopIteration:
            print()
            break