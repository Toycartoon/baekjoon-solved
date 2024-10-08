from itertools import permutations as p

while True:
    try:
        s, n = input().split()
        
        gen = p([*s], len(s))
        for i in range(int(n)-1):
            next(gen)
        
        print(s, n, "=", "".join(next(gen)))
    except EOFError:
        break
    except StopIteration:
        print(s, n, "= No permutation")