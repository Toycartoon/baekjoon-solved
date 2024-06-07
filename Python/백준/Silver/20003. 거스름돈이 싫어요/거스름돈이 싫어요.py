from math import lcm, gcd

n = int(input())

nume = []
deno = []
for _ in range(n):
    a, b = map(int, input().split())
    g = gcd(a, b)

    nume.append(a // g)
    deno.append(b // g)


g = gcd(gcd(*nume), lcm(*deno))
print(gcd(*nume) // g, lcm(*deno) // g)
