from collections import deque


s = input()
n = int(input())
ans = 0
for _ in range(n):
    i = deque([*input()])
    
    for x in range(len(i)):
        if list(i)[:len(s)] == [*s]:
            ans += 1
            break
        i.rotate(1)

print(ans)