i, re = 0, 0


def recursion(s, l, r):
    global re, i
    if l >= r:
        i += 1
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        re += 1
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    global re
    re += 1
    return recursion(s, 0, len(s)-1)


for _ in range(int(input())):
    i, re = 0, 0
    isPalindrome(input())
    print(i, re)
