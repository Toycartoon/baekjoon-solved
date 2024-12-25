import sys
import re

input = sys.stdin.readline

for t in range(int(input())):
    a, b = input().strip().split()

    if a == b:
        print(f"Case {t+1}: Login successful.")
    elif a == b.swapcase():
        print(f"Case {t+1}: Wrong password. Please, check your caps lock key.")
    elif re.sub(r'\d', '', a) == b:
        print(f"Case {t+1}: Wrong password. Please, check your num lock key.")
    elif re.sub(r'\d', '', a).swapcase() == b:
        print(f"Case {t+1}: Wrong password. Please, check your caps lock and num lock keys.")
    else:
        print(f"Case {t+1}: Wrong password.")
