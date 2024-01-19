import asyncio

async def primeira_corrotina():
    print("Inicio da primeira corrotina...")
    await asyncio.sleep(2)
    print("Fim da primeira corrotina...")

async def segunda_corrotina():
    print("Inicio da segunda corrotina...")
    await asyncio.sleep(3)
    print("Fim da segunda corrotina...")

async def terceira_corrotina():
    print("Inicio da terceira corrotina...")
    await asyncio.sleep(1)
    print("Fim da terceira corrotina...")


async def executa_corrotinas():
    print("==========Inicio do programa============")
    task_1 = asyncio.create_task(primeira_corrotina())
    task_2 = asyncio.create_task(segunda_corrotina())
    task_3 = asyncio.create_task(terceira_corrotina())
    await asyncio.gather(task_1, task_2, task_3)
    print("==========Fim do programa===============")

asyncio.run(executa_corrotinas())