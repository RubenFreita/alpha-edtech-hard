import asyncio

async def cinema(sem, nome_comprador):
    async with sem:
        print(f"{nome_comprador} escolhendo poltrona")
        await asyncio.sleep(2)
        print(f"{nome_comprador} finalizando compra")

async def main():
    sem = asyncio.Semaphore(1)
    clientes = ["Ruben", "Matheus", "Júlia", "Maria"]
    tasks = [cinema(sem, f"Cliente {nome}") for nome in clientes]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())