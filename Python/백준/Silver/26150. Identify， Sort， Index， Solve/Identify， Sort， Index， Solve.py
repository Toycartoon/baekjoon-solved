ans = ""
l = []
for _ in range(int(input())):
    s, i, d = input().split()
    l.append((s, int(i), int(d)))

l.sort(key=lambda x: x[1])
for si, ii, di in l:
    ans += si[di-1].upper()

print(ans)
