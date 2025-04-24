k = int(input())

time = 0
for n in range(int(input())):
    t, z = input().split()

    if time + int(t) >= 210:
        print(k % 8 if k % 8 != 0 else 8)
        break
    else:
        time += int(t)
        if z == 'T':
            k += 1
