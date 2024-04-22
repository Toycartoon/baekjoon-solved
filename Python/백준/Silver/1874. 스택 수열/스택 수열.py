n = int(input())

to_make = []
for _ in range(n):
    to_make.append(int(input()))

s = []
act = []
now = 0
add = 1
while now < n:
    if len(s) == 0 or to_make[now] > s[len(s) - 1]:
        s.append(add)
        add += 1
        act.append("+")
    elif to_make[now] == s[len(s) - 1]:
        s.pop()
        act.append("-")
        now += 1
    else:
        print("NO")
        exit(0)

for a in act:
    print(a)
