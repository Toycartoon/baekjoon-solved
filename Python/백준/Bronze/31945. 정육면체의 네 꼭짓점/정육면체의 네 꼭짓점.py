for t in range(int(input())):
    l = list(map(int, input().split()))
    l.sort()
    if l == [2, 3, 6, 7] or l == [1, 3, 5, 7] or l == [4, 5, 6, 7] or l == [0, 1, 4, 5] or l == [0, 1, 2, 3] or l == [0, 2, 4, 6]:
        print("YES")
    else:
        print("NO")