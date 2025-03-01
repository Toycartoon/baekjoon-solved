n = int(input())

for i in range(n, 3, -1):
    if {*str(i)} - {"4", "7"} == set():
        print(i)
        break
