w = {}
for n in range(int(input())):
    k = input().split()
    w[k[0]] = k[-1]

for i in range(int(input())):
    n = int(input())
    s = input().split()

    for x in s:
        print(w[x], end=" ")
    print()
