"""
Entrada: O seu programa receberá um número inteiro não negativo N que denota a quantidade de 
números que seu programa receberá para computar o valor total da soma. Na sequência seu 
programa receberá N números reais.

Saída: O seu programa deve imprimir a frase “Total:  ” seguida do valor da soma 
(com duas casas decimais de precisão).
"""

N = int(input("Informe o total de número que quer somar: "))
soma = 0
for i in range(N):
    
    soma += float(input("Informe o número que deseja incluir na soma: ").replace(",","."))

print(f"Total = {soma:.2f}")

