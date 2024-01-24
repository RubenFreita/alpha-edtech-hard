import asyncio
import concurrent.futures


def fatorial():
    n = 10
    print(f"\nCalculando o fatorial de {n}... ")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def escrever_txt():
    nome_arquivo = "arquivo"
    with open(nome_arquivo+".txt", "w") as arquivo:
        arquivo.write("escrevendo algo no arquivo txt")
    return "arquivo escrito com sucesso"

async def operacao_intensiva_processo():
    loop = asyncio.get_event_loop()

    with concurrent.futures.ProcessPoolExecutor() as pool:
        resultado1 = await loop.run_in_executor(pool, fatorial)
        print("Resultado do fatorial usando processo é: ", resultado1)
        resultado2 = await loop.run_in_executor(pool, escrever_txt)
        print("Resultado usando processo é: ", resultado2)


async def operacao_io_thread():
    loop = asyncio.get_event_loop()

    
    with concurrent.futures.ThreadPoolExecutor() as pool:
        resultado1 = await loop.run_in_executor(pool, fatorial)
        print("Resultado do fatorial usando thread é: ", resultado1)
        resultado2 = await loop.run_in_executor(pool, escrever_txt)
        print("Resultado usando thread é: ", resultado2)

async def main():
    await asyncio.gather(operacao_intensiva_processo(), operacao_io_thread())

if __name__ == "__main__":
    asyncio.run(main())