def hash_function(key):
    return sum(
         index * ord(character)
         for index, character in enumerate(repr(key), start=1)
     )


print(hash_function("Pequeno"))
print(hash_function("Uma frase de tamanho medio e sem acentos"))
print(hash_function("Uma frase muito, muito longa" * 1_000_000))

print(hash_function("Pequeno") % 17)
print(hash_function("Uma frase de tamanho medio e sem acentos") % 17)
print(hash_function("Uma frase muito, muito longa" * 1_000_000) % 17)
