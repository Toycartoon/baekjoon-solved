import re

p = re.compile("(100+1+|01)+")

if p.fullmatch(input()):
    print("SUBMARINE")
else:
    print("NOISE")