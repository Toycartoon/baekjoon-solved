n, s = input().split()
w = set()

ans = ""
x = 0
for i in s:
    if i in w:
        x += 1
    else:
        w.add(i)
        ans += i

ans += str(x+4)
ans = str(int(n) + 1906) + ans
ans = "smupc_" + ans[::-1]
print(ans)
