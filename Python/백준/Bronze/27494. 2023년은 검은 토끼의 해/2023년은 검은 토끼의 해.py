import re
a = 0
for i in range(1, int(input()) + 1):
    if re.search("2.*0.*2.*3.*", str(i)):
        a += 1
    
print(a)