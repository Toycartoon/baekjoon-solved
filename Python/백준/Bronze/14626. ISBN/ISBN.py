s = [*input()]

for ans in range(10):
    v = 0
    m = int(s[-1]) if int(s[-1]) != 0 else 10
    for i in range(len(s[:-1])):
        if i % 2 == 0:
            v += int(s[i]) if s[i] != "*" else ans
        else:
            v += 3 * int(s[i]) if s[i] != "*" else ans * 3

    if 10 - v % 10 == m:
        print(ans)
        break
