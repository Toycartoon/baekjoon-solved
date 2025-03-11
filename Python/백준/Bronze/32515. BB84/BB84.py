n = int(input())
jb = input()
jk = input()
ib = input()
ik = input()

ans = ""

for i in range(n):
    if jb[i] == ib[i]:
        if jk[i] == ik[i]:
            ans += jk[i]
        else:
            print("htg!")
            exit()

print(ans)
