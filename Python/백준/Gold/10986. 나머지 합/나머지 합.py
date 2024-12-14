# Special Thanks : iktk, jshyun912

n, m = map(int, input().split())
a = list(map(int, input().split()))

ps = [0]
t = 0
for i in a:
    t += i
    ps.append(t % m)


ans = 0
l = [0 for _ in range(m)]
for i in range(1, n+1):
    l[ps[i]] += 1

for i in range(1, n+1):
    ans += l[ps[i-1]]
    l[ps[i]] -= 1

print(ans)
