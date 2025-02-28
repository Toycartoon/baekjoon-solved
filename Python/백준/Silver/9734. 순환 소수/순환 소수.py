import re
import sys
from math import gcd, lcm

input = sys.stdin.readline

def repeating_decimal(x):
    deno = int("9" * len(x.split("(")[1][:-1]) + "0" * len(x.split(".")[1].split("(")[0]))
    mole = int(re.sub(r"\D+", "", x)) - int(re.sub(r"\D+", "", x.split("(")[0]))

    return mole, deno


def decimal(x):
    return int(re.sub(r"\D+", "", x)), 10 ** len(x.split(".")[1])


while True:
    try:
        s = input().strip()

        if "(" in s:
            frac_s = repeating_decimal(s)
        else:
            frac_s = decimal(s)

        g = gcd(frac_s[0], frac_s[1])
        print(f"{s} = {frac_s[0] // g} / {frac_s[1] // g}")
    except ValueError:
        break
