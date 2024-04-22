from math import factorial as f

n = int(input())
print(str(f(n)).strip("0")[-1])