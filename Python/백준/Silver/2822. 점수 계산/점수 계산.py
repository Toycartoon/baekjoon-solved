# https://www.acmicpc.net/problem/2822
score = []
for _ in range(8):
    score.append(int(input()))

ms = 0
q = []
for _ in range(5):
    best = max(score)
    ms += best
    q.append(str(score.index(best) + 1))
    score[score.index(best)] = -1

print(ms)
print(" ".join(sorted(q)))
