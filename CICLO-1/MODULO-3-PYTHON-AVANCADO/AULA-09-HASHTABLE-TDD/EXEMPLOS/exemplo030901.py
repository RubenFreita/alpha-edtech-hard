import string
texto = string.ascii_uppercase * 100_000_000

print(len(texto))

print(texto[30_000_000:30_000_050])
