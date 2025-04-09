n = int(input())
s = input()

ans = 1
x = 0
while ans < n:
    if s[x:x+len(str(ans))] != str(ans):
        print(ans)
        exit()

    x += len(str(ans))
    ans += 1

print(n)
