#Questão 09

angulo = float(input("Digite o angulo entre as localidades C1 e C2: "))
distanciaEstadios = float(input("Digite a distancia em estádios entre as localidades C1 e C2: "))



tamPlanetaEmEstadios = (distanciaEstadios*360)/angulo

distanciaKm = (distanciaEstadios*176.4)/1000 #em km

tamPlanetaEmKm = (distanciaKm*360)/angulo

print(f"O Tamanho do planeta em estádios é: {tamPlanetaEmEstadios} Estádios")
print(f"O Tamanho do planeta em KM é: {tamPlanetaEmKm} KM")
