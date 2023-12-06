

def teste_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    for i in args:
        print(i)





print("==========")
teste_args("Carro", 100, 50, "pedra")

print()
print("==========")
teste_args("brasil", "País",  "Mundo", "Carro", 100, 50, "pedra")

print()
print("==========")
teste_args("brasil", "País",  "Gol", "Carro", 10)