# Baekjoon 10866

from sys import stdin, stdout

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
n = int(stdin.readline())

d = []
for _ in range(n):
    com = stdin.readline()
    if 'push_front' in com:
        d.insert(0, int(com.split()[1]))
    elif 'push_back' in com:
        d.append(int(com.split()[1]))
    elif 'pop_front' in com:
        try:
            stdout.write(str(d.pop(0)) + "\n")
        except IndexError:
            stdout.write("-1\n")
    elif 'pop_back' in com:
        try:
            stdout.write(str(d.pop()) + "\n")
        except IndexError:
            stdout.write("-1\n")
    elif 'size' in com:
        stdout.write(str(len(d)) + "\n")
    elif 'empty' in com:
        if len(d) == 0:
            stdout.write("1\n")
        else:
            stdout.write("0\n")
    elif 'front' in com:
        try:
            stdout.write(str(d[0]) + "\n")
        except IndexError:
            stdout.write("-1\n")
    else:
        try:
            stdout.write(str(d[len(d) - 1]) + "\n")
        except IndexError:
            stdout.write("-1\n")
