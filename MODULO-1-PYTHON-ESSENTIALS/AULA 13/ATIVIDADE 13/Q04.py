
def cpf_valido(cpf):
    cpf = "".join(str(cpf).replace(".","").replace("-",""))
    
    soma_primeiro = 0
    j = 10
    for i in range(len(cpf)-2):
        soma_primeiro += j*int(cpf[i])
        j -= 1
    soma_segundo = 0
    j = 11
    for i in range(len(cpf)-1):
        soma_segundo += j*int(cpf[i])
        j -= 1
    
    
    resto_primeiro = soma_primeiro % 11
    resto_segundo = soma_segundo % 11
    if (11 - resto_primeiro >= 10 and int(cpf[-2]) == 0) or 11 - resto_primeiro == int(cpf[-2]):
        if (11 - resto_segundo >= 10 and int(cpf[-1]) == 0) or 11 - resto_segundo == int(cpf[-1]):
            return "é válido"
    return "não é válido"

cpf = "145.382.206-20"
print(f"O CPF {cpf} {cpf_valido(cpf)}")
cpf = "900.565.823-15"
print(f"O CPF {cpf} {cpf_valido(cpf)}")
cpf = "795.631.123-34"
print(f"O CPF {cpf} {cpf_valido(cpf)}")
cpf = "075.097.234-23"
print(f"O CPF {cpf} {cpf_valido(cpf)}")