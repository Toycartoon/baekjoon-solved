i = 1
while True:
    s = input()
    if s.split()[1] == "E":
        break
    
    print(f"Case {i}: {str(eval(s)).lower()}")
    i += 1