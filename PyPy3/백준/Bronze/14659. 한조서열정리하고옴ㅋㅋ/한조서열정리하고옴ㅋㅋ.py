import sys

n = int(sys.stdin.readline())
peaks = sys.stdin.readline().split()

for _ in range(n):
    peaks[_] = int(peaks[_])

potg = 0
for i in range(n):
    kc = 0
    for j in range(i + 1, n):
        if peaks[i] >= peaks[j]:
            kc += 1
        else:
            break
        if kc > potg:
            potg = kc

sys.stdout.write(str(potg))
