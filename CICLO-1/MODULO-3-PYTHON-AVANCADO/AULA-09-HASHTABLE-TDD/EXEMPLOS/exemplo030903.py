def hash_function(key):
    for index, character in enumerate(repr(key), start=1):
        print(index, character, sep=" - ", end="; ")
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start=1)
    )


print(hash_function('Lorem'))
print(hash_function("Loren"))
print(hash_function("Loner"))
