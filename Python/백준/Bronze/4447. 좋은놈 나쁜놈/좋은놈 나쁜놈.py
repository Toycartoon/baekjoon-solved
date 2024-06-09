for t in range(int(input())):
    s = input()
    g = s.lower().count("g")
    b = s.lower().count("b")
    
    if g > b:
        print(f"{s} is GOOD")
    elif g < b:
        print(f"{s} is A BADDY")
    else:
        print(f"{s} is NEUTRAL")