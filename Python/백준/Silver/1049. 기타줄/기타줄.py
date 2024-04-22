n, m = map(int, input().split())

pack = []
thing = []

for i in range(m):
    P, O = map(int, input().split())
    pack.append(P)
    thing.append(O)

Pmin = min(pack)
Omin = min(thing)

if Pmin > 6 * Omin:
    print(n * Omin)
else:
    buy = Pmin * (n//6)
    remain = n % 6
    if Pmin > Omin * remain:
        buy += Omin * remain
    else:
        buy += Pmin

    print(buy)