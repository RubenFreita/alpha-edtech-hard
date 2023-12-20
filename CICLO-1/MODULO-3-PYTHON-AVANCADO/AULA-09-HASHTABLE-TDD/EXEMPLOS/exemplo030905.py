import hashlib
print(hash("3.14"))
print(hash(3.14))
print(hash("a"), hash("b"), hash("c"))

h = hashlib.sha256(b"3.14")
print(h.digest())