

populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015
count = 0
while populacaoA<populacaoB:
    count +=1
    populacaoA = populacaoA*crescimentoA
    populacaoB = populacaoB*crescimentoB

print(f"O país A levará {count} anos para ultrapassar ou igualar o total de habitantes do país B.")