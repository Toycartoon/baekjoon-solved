ipv6 = input().split(":")

if ipv6[0] == "":
    ipv6 = ipv6[1:]
elif ipv6[-1] == "":
    ipv6 = ipv6[:-1]


s = []
for i in ipv6:
    if i == "":
        for x in range(8-len(ipv6)+1):
            s.append("0000")
    else:
        s.append(i.zfill(4))


print(":".join(s))
