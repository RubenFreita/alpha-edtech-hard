def cnpj_valido(cnpj):
    cnpj = "".join(str(cnpj).replace(".","").replace("-","").replace("/",""))
    
    soma_primeiro = 0
    j = 2
    for i in range(-3, -15,-1):
        soma_primeiro += j*int(cnpj[i])
        j+=1
        if(j == 10):
            j=2

    soma_segundo = 0
    j = 2
    for i in range(-2, -15,-1):
        soma_segundo += j*int(cnpj[i])
        j+=1
        if(j == 10):
            j=2
    
    resto_primeiro = soma_primeiro % 11
    resto_segundo = soma_segundo % 11

    if (11 - resto_primeiro >= 10 and int(cnpj[-2]) == 0) or 11 - resto_primeiro == int(cnpj[-2]):
        if (11 - resto_segundo >= 10 and int(cnpj[-1]) == 0) or 11 - resto_segundo == int(cnpj[-1]):
            return "é válido"
    return "não é válido"
    

cnpj = "59.541.264/0001-03"
print(f"O cnpj {cnpj} {cnpj_valido(cnpj)}")
cnpj = "31.813.719/0001-75"
print(f"O cnpj {cnpj} {cnpj_valido(cnpj)}")
cnpj = "18.518.134/0001-64"
print(f"O cnpj {cnpj} {cnpj_valido(cnpj)}")
cnpj = "28.464.744/0001-80"
print(f"O cnpj {cnpj} {cnpj_valido(cnpj)}")