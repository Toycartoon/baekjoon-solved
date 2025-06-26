n = int(input())
s = input()
print(n-max(s.count("E"), s.count("W"), s.count("N"), s.count("S")))
