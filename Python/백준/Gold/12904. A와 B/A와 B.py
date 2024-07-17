import sys

sys.setrecursionlimit(10 ** 6)

s = input()
t = input()


ans = 0
def backtracking(x):
    global ans
    
    if len(x) == len(s):
        if x == s:
            ans = 1
            return
    else:
        if x[-1] == "A":
            backtracking(x[:-1])
        else:
            backtracking(x[:-1][::-1])


backtracking(t)
print(ans)
