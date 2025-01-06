alphabet = input("")
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]
ans = []

for i in croatia:
    alphabet = alphabet.replace(i, '+')

print(len(alphabet))