from math import gcd


def diff(terms):
    new_terms = []
    for x, degree in terms:
        if x == "":
            continue
        if x[0] == "+":
            x = x[1:]

        if degree == 0:
            continue
        elif degree == 1:
            new_terms.append((x, 0))
            continue

        if "/" in x:
            num, deno = x.split("/")
            num = int(num) * degree
            g = gcd(num, int(deno))
            num //= g
            deno = int(deno) // g

            if deno == 1:
                new_terms.append((str(num), degree - 1))
            else:
                new_terms.append((f"{num}/{deno}", degree - 1))
        else:
            if x == "-" or x == "":
                x += "1"
            new_terms.append((str(int(x) * degree), degree - 1))


    return new_terms


for _ in range(int(input())):
    i, m = input().split()

    terms = []
    s = ""
    rank = ""
    for x in i:
        if x == "x":
            rank = s
            if rank == "" or rank == "-":
                rank += "1"
            s = ""
        elif x == "+" or x == "-":
            terms.append((rank, int(s[1:]) if s[1:] != "" else 1))
            s = x
        else:
            s += x
    terms.append((s, 0))

    for _ in range(2):
        terms = diff(terms)


    compare_m = ""
    if terms == []:
        compare_m += "0"

    for rank, degree in terms:
        if degree == 0:
            if rank[0] != "-" and len(compare_m) != 0:
                rank = "+" + rank
            compare_m += rank
        elif degree == 1:
            if rank == "1":
                if len(compare_m) != 0:
                    compare_m += "+"
                compare_m += "x"
            elif rank == "-1":
                compare_m += "-x"
            else:
                if rank[0] != "-" and len(compare_m) != 0:
                    rank = "+" + rank
                compare_m += rank + "x"
        else:
            if rank == "1":
                if len(compare_m) != 0:
                    compare_m += "+"
                compare_m += "x^" + str(degree)
            elif rank == "-1":
                compare_m += "-x^" + str(degree)
            else:
                if len(compare_m) != 0 and rank[0] != "-":
                    compare_m += "+"
                compare_m += rank + "x^" + str(degree)

    if compare_m == m:
        print("Yes")
    else:
        print("No")
