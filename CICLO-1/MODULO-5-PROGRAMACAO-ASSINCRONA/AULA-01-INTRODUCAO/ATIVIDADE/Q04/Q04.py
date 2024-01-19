import asyncio

async def primeira_corrotina(evento: asyncio.Event):
    print("Inicio da primeira corrotina...")
    print("Esperando evento...")
    await evento.wait()
    print("Evento finalizado...")
    print("Fim da primeira corrotina...")

async def segunda_corrotina(evento: asyncio.Event):
    print("Inicio da segunda corrotina...")
    print("Segunda corrotina, sinalizando evento...")
    evento.set()
    print("Fim da segunda corrotina...")

async def executa_corrotinas():
    evento = asyncio.Event()
    tarefa_1 = asyncio.create_task(primeira_corrotina(evento))
    tarefa_2 = asyncio.create_task(segunda_corrotina(evento))

    await asyncio.gather(tarefa_1, tarefa_2)

asyncio.run(executa_corrotinas())
