import sys

sys.set_int_max_str_digits(10 ** 6)
for t in range(int(input())):
    n = int(input())
    print(11 * int("1"*(n-1) if n-1 != 0 else 0))