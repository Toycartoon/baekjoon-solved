import re

p = re.compile("da+dd?(i|y)")
while True:
    try:
        if p.fullmatch(input()):
            print("She called me!!!")
        else:
            print("Cooing")
    except EOFError:
        break