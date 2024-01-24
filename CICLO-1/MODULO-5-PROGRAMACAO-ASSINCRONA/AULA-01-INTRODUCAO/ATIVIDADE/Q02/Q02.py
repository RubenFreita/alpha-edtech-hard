import asyncio

async def primeira_corrotina():
    print("Inicio da primeira corrotina...")
    await asyncio.sleep(3)
    print("Fim da primeira corrotina...")
    return "retorno da primeira corrotina"

async def segunda_corrotina():
    print("Inicio da segunda corrotina...")
    await asyncio.sleep(2)
    print("Fim da segunda corrotina...")
    return "retorno da segunda corrotina"

async def executa_corrotinas():
    
    task_1 = asyncio.create_task(primeira_corrotina())
    task_2 = asyncio.create_task(segunda_corrotina())
    retorno1 = await task_1
    retorno2 = await task_2
    # print(retorno1, retorno2)
asyncio.run(executa_corrotinas())