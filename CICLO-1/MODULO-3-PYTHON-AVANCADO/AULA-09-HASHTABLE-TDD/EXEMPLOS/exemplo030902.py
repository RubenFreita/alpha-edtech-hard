def hash_function(key):
    return sum(ord(character) for character in repr(key))

print(hash_function("3.14"))
print(hash_function(3.14))
print(hash_function("Lorem"))
print(hash_function("Loren"))
print(hash_function("Loner"))
print(hash_function(True))
