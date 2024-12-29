import re
from math import gcd, lcm


def repeating_decimal(x):
    deno = int("9" * len(x.split("(")[1][:-1]) + "0" * len(x.split(".")[1].split("(")[0]))
    mole = int(re.sub(r"\D+", "", x)) - int(re.sub(r"\D+", "", x.split("(")[0]))

    return mole, deno


def decimal(x):
    return int(re.sub(r"\D+", "", x)), 10 ** len(x.split(".")[1])


a = input()
b = input()

frac_a = []
frac_b = []
if "(" in a:
    frac_a = repeating_decimal(a)
elif "." in a:
    frac_a = decimal(a)
else:
    frac_a = [int(a), 1]

if "(" in b:
    frac_b = repeating_decimal(b)
elif "." in b:
    frac_b = decimal(b)
else:
    frac_b = [int(b), 1]


ans = [0, 0]
ans[1] = lcm(frac_a[1], frac_b[1])
ans[0] = (ans[1] // frac_a[1]) * frac_a[0] + (ans[1] // frac_b[1]) * frac_b[0]

g = gcd(ans[0], ans[1])
print(f"{ans[0] // g}/{ans[1] // g}")
