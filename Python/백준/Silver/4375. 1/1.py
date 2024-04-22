while True:
    try:
        n = int(input())
        i = 1
        while True:
            if int("1" * i) % n == 0:
                print(i)
                break
            i += 1
    except:
        break