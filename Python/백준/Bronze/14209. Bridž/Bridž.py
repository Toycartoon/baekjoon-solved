n = int(input())
ans = 0

for i in range(n):
    s = input()
    ans += s.count("A") * 4 + s.count("K") * 3 + s.count("Q") * 2 + s.count("J")

print(ans)
