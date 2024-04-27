while True:
    try:
        s = input()
        a = [0, 0, 0, 0]
    
        for _ in s:
            if _.isupper():
                a[1] += 1
            elif _.islower():
                a[0] += 1
            elif _.isspace():
                a[3] += 1
            else:
                a[2] += 1
    
        for i in range(4):
            a[i] = str(a[i])
        print(" ".join(a))
    except EOFError:
        break