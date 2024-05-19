from collections import deque

s = input()
q = deque([*input()])

front, back = [], []

is_front = True
while q:
    if is_front:
        front.append(q.popleft())
        if front[len(front)-len(s):] == [*s]:
            for i in range(len(s)):
                front.pop()
            is_front = False
    else:
        back.append(q.pop())
        if back[len(back)-len(s):] == [*s][::-1]:
            for i in range(len(s)):
                back.pop()
            is_front = True


front.extend(back[::-1])
ans = []

q = deque(front)
while q:
    ans.append(q.popleft())
    if ans[len(ans)-len(s):] == [*s]:
        for i in range(len(s)):
            ans.pop()

print("".join(ans))
