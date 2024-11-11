n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
memo = set()


def bt(l):
    if len(l) == m:
        if tuple(sorted(l)) not in memo:
            for i in l:
                print(i, end=" ")
                memo.add(tuple(sorted(l)))
            print()

    for i in a:
        if i not in l or l.count(i) != a.count(i):
            bt(l + [i])


bt([])
