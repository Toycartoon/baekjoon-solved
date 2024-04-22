for i in range(int(input())):
    _ = input()
    s = list(input())
    s.sort(reverse=True)
    
    a = int("".join(s[:len(s) - 1]))
    b = int(s[len(s) - 1])

    print(a + b)