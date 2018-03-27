import hashlib
msg=hashlib.sha1(b"Hello Word").digest()
print(msg)
