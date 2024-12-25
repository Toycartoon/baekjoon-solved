s = input().split()
t = len(s)
ae = 0

for i in s:
    if "ae" in i:
        ae += 1

if t * 0.4 <= ae:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
