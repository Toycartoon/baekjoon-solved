n, m = map(int, input().split())
if m > 6 and n > 2:
    print(m-2)
elif n == 2:
    print(min((m+1)//2, 4))
elif n == 1:
    print(1)
else:
    print(min(m, 4))