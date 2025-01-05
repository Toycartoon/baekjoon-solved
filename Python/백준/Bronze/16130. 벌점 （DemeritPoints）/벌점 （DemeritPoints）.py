import sys

input = sys.stdin.readline

for t in range(int(input())):
    s = input().strip()

    sum = 0
    ans = 0
    m = 0
    st = ""
    for i in s:
        if i.isalpha():
            sum += ord(i) - 55
        else:
            sum += int(i)

        if sum // 10 > 4:
            st = "(09)"
            break
        elif sum // 10 == 4:
            st = "(weapon)"
            break

        if m < sum // 10:
            m = sum // 10
            ans += sum // 10

    print(str(ans)+st)
