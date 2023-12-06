

def is_palindromo(frase):
    frase_sem_espaco = "".join(frase.split())
    fraseInversa = frase_sem_espaco[::-1]
    
    if frase_sem_espaco.lower() == fraseInversa.lower():
        print(f"A frase \"{frase}\" é palíndromo")
    else:
        print(f"A frase \"{frase}\" não é palíndromo")
    

frase1 = "anilina"
is_palindromo(frase1)
    
frase2 = "A dama admirou o rim da amada"
is_palindromo(frase2)

frase3 = "Luza Rocelina a namorada do Manuel leu na moda da romana anil e cor azul"
is_palindromo(frase3)

frase3 = "joao e alto"
is_palindromo(frase3)