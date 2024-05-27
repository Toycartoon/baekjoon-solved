n = int(input())
k = input()
odd, even = 0, 0

for i in k:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

if odd > even:
    print(1)
elif even > odd:
    print(0)
else:
    print(-1)
