import sys

input = sys.stdin.readline

k = ["063", "010", "093", "079", "106", "103", "119", "011", "127", '107']

while True:
    s = input().strip()

    if s == "BYE":
        break

    a, b = s.split("+")
    b = b[:-1]

    ai, bi = "", ""
    for i in range(2, len(a), 3):
        ai += str(k.index(a[i-2:i+1]))

    for i in range(2, len(b), 3):
        bi += str(k.index(b[i-2:i+1]))

    ci = int(ai) + int(bi)
    c = ""
    for i in str(ci):
        c += k[int(i)]

    print(f"{a}+{b}={c}")
