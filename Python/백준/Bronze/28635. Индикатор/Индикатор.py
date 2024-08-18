m = int(input())
a = int(input())
b = int(input())

ans = 0
while a != b:
    a += 1
    if a > m:
        a -= m
    
    ans += 1

print(ans)