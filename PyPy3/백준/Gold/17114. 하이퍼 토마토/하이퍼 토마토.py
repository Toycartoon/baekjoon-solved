import collections

input = iter(open(0).read().split('\n')).__next__

m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
graph = []
deq = collections.deque()
ans = -1
zero_count = 0

for _ in range(w):
    l1 = []
    for __ in range(v):
        l2 = []
        for ___ in range(u):
            l3 = []
            for ____ in range(t):
                l4 = []
                for _____ in range(s):
                    l5 = []
                    for ______ in range(r):
                        l6 = []
                        for _______ in range(q):
                            l7 = []
                            for ________ in range(p):
                                l8 = []
                                for _________ in range(o):
                                    l9 = []
                                    for __________ in range(n):
                                        l9.append(list(map(int, input().split())))
                                    l8.append(l9)
                                l7.append(l8)
                            l6.append(l7)
                        l5.append(l6)
                    l4.append(l5)
                l3.append(l4)
            l2.append(l3)
        l1.append(l2)
    graph.append(l1)


for a in range(w):
    for b in range(v):
        for c in range(u):
            for d in range(t):
                for e in range(s):
                    for f in range(r):
                        for g in range(q):
                            for h in range(p):
                                for i in range(o):
                                    for j in range(n):
                                        for k in range(m):
                                            if graph[a][b][c][d][e][f][g][h][i][j][k] == 1:
                                                deq.append((a, b, c, d, e, f, g, h, i, j, k, 0))
                                            if graph[a][b][c][d][e][f][g][h][i][j][k] == 0:
                                                zero_count += 1


def pos(a, b, c, d, e, f, g, h, i, j, k, day):
    global zero_count


    if 0 > a or a >= w:
        return
    if 0 > b or b >= v:
        return
    if 0 > c or c >= u:
        return
    if 0 > d or d >= t:
        return
    if 0 > e or e >= s:
        return
    if 0 > f or f >= r:
        return
    if 0 > g or g >= q:
        return
    if 0 > h or h >= p:
        return
    if 0 > i or i >= o:
        return
    if 0 > j or j >= n:
        return
    if 0 > k or k >= m:
        return

    if graph[a][b][c][d][e][f][g][h][i][j][k] == 1 or graph[a][b][c][d][e][f][g][h][i][j][k] == -1:
        return

    deq.append((a, b, c, d, e, f, g, h, i, j, k, day+1))
    graph[a][b][c][d][e][f][g][h][i][j][k] = 1
    zero_count -= 1
    return


while deq:
    _w, _v, _u, _t, _s, _r, _q, _p, _o, _n, _m, day = deq.popleft()

    if day > ans:
        ans = day

    pos(_w-1, _v, _u, _t, _s, _r, _q, _p, _o, _n, _m, day)
    pos(_w+1, _v, _u, _t, _s, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v-1, _u, _t, _s, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v+1, _u, _t, _s, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u-1, _t, _s, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u+1, _t, _s, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t-1, _s, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t+1, _s, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s-1, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s+1, _r, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r-1, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r+1, _q, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q-1, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q+1, _p, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q, _p-1, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q, _p+1, _o, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q, _p, _o-1, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q, _p, _o+1, _n, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q, _p, _o, _n-1, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q, _p, _o, _n+1, _m, day)
    pos(_w, _v, _u, _t, _s, _r, _q, _p, _o, _n, _m-1, day)
    pos(_w, _v, _u, _t, _s, _r, _q, _p, _o, _n, _m+1, day)


if zero_count != 0:
    print(-1)
else:
    print(ans)
