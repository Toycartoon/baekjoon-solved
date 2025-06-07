y = "YONSEI."
k = "KOREA."

kx, yx = 0, 0
s = input()
for i in s:
    if i == k[kx]:
        kx += 1
        if k[kx] == ".":
            print(k[:-1])
            break
    if i == y[yx]:
        yx += 1
        if y[yx] == ".":
            print(y[:-1])
            break
