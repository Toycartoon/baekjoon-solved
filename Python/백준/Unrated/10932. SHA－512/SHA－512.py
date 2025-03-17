import hashlib

sha = hashlib.sha512()
sha.update(input().encode())
print(sha.hexdigest())