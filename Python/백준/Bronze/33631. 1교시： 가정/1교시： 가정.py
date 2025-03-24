fs, cs, es, bs = map(int, input().split())
fn, cn, en, bn = map(int, input().split())

c = 0
for _ in range(int(input())):
    q, i = map(int, input().split())

    if q == 1:
        if fn * i <= fs and cn * i <= cs and en * i <= es and bn * i <= bs:
            c += i

            fs -= fn * i
            cs -= cn * i
            es -= en * i
            bs -= bn * i
            print(c)
        else:
            print("Hello, siumii")
    elif q == 2:
        fs += i
        print(fs)
    elif q == 3:
        cs += i
        print(cs)
    elif q == 4:
        es += i
        print(es)
    elif q == 5:
        bs += i
        print(bs)
