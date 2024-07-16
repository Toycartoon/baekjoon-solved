import sys

input = sys.stdin.readline


def update(tree, i, val):
    i += len(tree) // 2 - 1
    tree[i] = val

    while i > 1:
        i //= 2
        tree[i] = tree[i * 2] * tree[i * 2 + 1]


def query(tree, i, j):
    ans = 1

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j:
        if i % 2 == 1:
            ans *= tree[i]
            i += 1
        if j % 2 == 0:
            ans *= tree[j]
            j -= 1

        i //= 2
        j //= 2

    return ans


while True:
    try:
        n, m = map(int, input().split())
        tree = [0 for _ in range(n)]

        a = list(map(int, input().split()))
        for i in a:
            if i > 0:
                tree.append(1)
            elif i < 0:
                tree.append(-1)
            else:
                tree.append(0)

        n = len(tree) // 2
        for i in range(n-1, 0, -1):
            tree[i] = tree[i * 2] * tree[i * 2 + 1]

        ans = ""
        for i in range(m):
            com, b, c = input().split()

            if com == "C":
                if int(c) > 0:
                    c = 1
                elif int(c) < 0:
                    c = -1
                else:
                    c = 0
                    
                update(tree, int(b), c)
            elif com == "P":
                v = query(tree, int(b), int(c))

                if v > 0:
                    ans += "+"
                elif v < 0:
                    ans += "-"
                else:
                    ans += "0"

        print(ans)
            
    except:
        break
