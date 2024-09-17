for t in range(int(input())):
    s = input()
    
    print(min(len(s) - s.count("a"), len(s) - s.count("b")))