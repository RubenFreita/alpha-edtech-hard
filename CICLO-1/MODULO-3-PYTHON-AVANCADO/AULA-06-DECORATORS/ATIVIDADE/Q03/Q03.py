


def divide_1(entrada: float) -> None:
    try:
        x = 1/entrada
    except ZeroDivisionError:
        print("Não foi possível realizar a divisão, pois a divisão de 1 por 0 é indefinida.")
    except TypeError:
        print("Não foi possível realizar a divisão, pois não é possível dividir um número int com outro tipo.")
    except:
        print("Não foi possível realizar a divisão.")
    else:
        print(f"A divisão de 1 por {entrada} é: {x}")
    finally:
        print("Meu nome é Ruben Freitas.")    

divide_1(0)
divide_1("oi")
divide_1(3)
divide_1(None)