for _ in range(int(input())):
    w = [0 for _ in range(26)]
    for i in input():
        w[ord(i)-97] += 1
    
    w.sort()
    print(sum(w[:-2]))
