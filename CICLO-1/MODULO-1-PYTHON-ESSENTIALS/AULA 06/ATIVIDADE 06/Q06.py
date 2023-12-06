


r = 1
ant = -1
atual = 1
limite = 500
while True:
    r = atual + ant
    ant = atual
    atual = r
    if r <= limite:
        print(f"{r}", end=", ")
    else:
        print(f"{r}.")
        break