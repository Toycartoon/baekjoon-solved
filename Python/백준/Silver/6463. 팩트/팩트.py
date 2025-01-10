import sys
from math import factorial as f

sys.set_int_max_str_digits(40000)

while True:
    try:
        n = int(input())
        print(str(n).rjust(5, " "), "->", str(int(str(f(n))[::-1]))[0])
    except EOFError:
        break
