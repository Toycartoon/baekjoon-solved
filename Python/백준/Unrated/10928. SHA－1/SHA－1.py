import hashlib

sha = hashlib.sha1()
sha.update(input().encode())
print(sha.hexdigest())
