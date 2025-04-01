while True:
    s = input()
    
    if s == "#":
        break
        
    vowel = 0
    for i in s:
        if i.lower() in ('a', 'e', 'i', 'o', 'u'):
            vowel += 1
    
    print(vowel)