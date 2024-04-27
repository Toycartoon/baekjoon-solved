n = int(input())
f = int(input())

for i in range(100):
    if int(str(n)[:len(str(n)) - 2] + str(i).zfill(2)) % f == 0:
        print(str(i).zfill(2))
        break
