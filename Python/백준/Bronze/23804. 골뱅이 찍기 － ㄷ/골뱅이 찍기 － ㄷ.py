# Baekjoon 23804

def d(n):
    for _ in range(n):
        print("@@@@@" * n)


n = int(input())

d(n)
for _ in range(3 * n):
    print("@" * n)
d(n)