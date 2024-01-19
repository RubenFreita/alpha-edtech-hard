import asyncio

async def primeira_corrotina():
    print("Inicio da primeira corrotina...")
    await asyncio.sleep(2)
    print("Fim da primeira corrotina...")

async def segunda_corrotina():
    print("Inicio da segunda corrotina...")
    await asyncio.sleep(3)
    print("Fim da segunda corrotina...")

async def executa_corrotinas():
    
    task_1 = await asyncio.create_task(primeira_corrotina())
    task_2 = await asyncio.create_task(segunda_corrotina())
    
asyncio.run(executa_corrotinas())