import asyncio

async def solicitacao():
    print("Inicio da solicitação...")
    await asyncio.sleep(2)
    print("Fim da solicitação...")

asyncio.run(solicitacao())

