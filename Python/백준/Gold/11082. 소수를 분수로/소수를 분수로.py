import re
from math import gcd


def repeating_decimal(x):
    deno = int("9" * len(x.split("(")[1][:-1]) + "0" * len(x.split(".")[1].split("(")[0]))
    mole = int(re.sub(r"\D+", "", x)) - int(re.sub(r"\D+", "", x.split("(")[0]))

    return mole, deno


def decimal(x):
    return int(re.sub(r"\D+", "", x)), 10 ** len(x.split(".")[1])


s = input().strip()

if "(" in s:
    frac_s = repeating_decimal(s)
elif "." in s:
    frac_s = decimal(s)
else:
    print(f"{s}/1")
    exit()

g = gcd(frac_s[0], frac_s[1])
print(f"{frac_s[0] // g}/{frac_s[1] // g}")
