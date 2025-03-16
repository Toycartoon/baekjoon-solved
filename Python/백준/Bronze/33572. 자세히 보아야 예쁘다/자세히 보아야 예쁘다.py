n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    m -= i-1

if m > 0:
    print("OUT")
else:
    print("DIMI")