import asyncio
import concurrent.futures as cf

def leitura_nome():
        print()
        nome = input("Digite seu nome: \n")
        return nome

def gasta_recurso():
    for _ in range(100000):
          a = "Só gastando tempo processamento mesmo..."
    return a

async def tarefa_processo():
    loop = asyncio.get_event_loop()

    with cf.ProcessPoolExecutor() as pool:
          resultado = await loop.run_in_executor(pool, gasta_recurso)
          print(f"Resultado do processo: {resultado}")

async def tarefa_thread():
    loop = asyncio.get_event_loop()

    with cf.ThreadPoolExecutor() as pool:
          resultado = await loop.run_in_executor(pool, leitura_nome)
          print(f"Resultado da thread: {resultado}")

async def tarefa_assincrona():
    print("Inicio da tarefa assincrona...")
    await asyncio.sleep(2)
    print("Fim da tarefa assincrona...")

async def main():
    tarefa_a = asyncio.create_task(tarefa_assincrona())
    await asyncio.gather(tarefa_a, tarefa_processo(), tarefa_thread())

if __name__ == "__main__":
    asyncio.run(main())