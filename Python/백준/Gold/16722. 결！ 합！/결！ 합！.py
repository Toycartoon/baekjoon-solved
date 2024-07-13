a = []
for _ in range(9):
    a.append(input().split())


all_a = set()
for i in range(9):
    for j in range(9):
        for k in range(9):
            if i == j or j == k or i == k:
                continue

            f = True
            for l in range(3):
                if not (a[i][l] == a[j][l] == a[k][l] or (a[i][l] != a[j][l] and a[i][l] != a[k][l] and a[j][l] != a[k][l])):
                    f = False

            if f:
                all_a.add(tuple(sorted([i, j, k])))


score = 0
f = True
for i in range(int(input())):
    com, *v = input().split()

    if com == "G":
        if len(all_a) == 0 and f:
            f = False
            score += 3
        else:
            score -= 1
    elif com == "H":
        if tuple(sorted([int(v[0])-1, int(v[1])-1, int(v[2])-1])) in all_a:
            all_a.remove(tuple(sorted([int(v[0])-1, int(v[1])-1, int(v[2])-1])))
            score += 1
        else:
            score -= 1


print(score)
