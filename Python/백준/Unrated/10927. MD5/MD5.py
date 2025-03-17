import hashlib

s = input()

md5 = hashlib.md5()
md5.update(s.encode())
print(md5.hexdigest())
