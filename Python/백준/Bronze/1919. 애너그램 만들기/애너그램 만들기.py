s1 = input()
s2 = input()

a = [0 for _ in range(26)]
for i in s1:
    a[ord(i)-97] += 1

for i in s2:
    a[ord(i)-97] -= 1

ans = 0
for i in a:
    ans += abs(i)

print(ans)
