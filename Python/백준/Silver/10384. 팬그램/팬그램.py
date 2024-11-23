for t in range(int(input())):
    w = [0 for _ in range(26)]
    
    s = input()
    for i in s:
        if i.isalpha():
            w[ord(i.upper())-65] += 1
    
    if min(w) >= 3:
        print(f"Case {t+1}: Triple pangram!!!")
    elif min(w) >= 2:
        print(f"Case {t+1}: Double pangram!!")
    elif min(w) >= 1:
        print(f"Case {t+1}: Pangram!")
    else:
        print(f"Case {t+1}: Not a pangram")