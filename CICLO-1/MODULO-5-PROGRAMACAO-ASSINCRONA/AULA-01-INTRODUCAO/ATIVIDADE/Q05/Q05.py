import asyncio as asc

class Sanduiche():
    def __init__(self, tipo_carne, qtd_blend) -> None:
        self._tipo_carne = tipo_carne
        self._qtd_blend = qtd_blend

    async def monta_sanduiche(self, evento: asc.Event):
        print("Iniciando montagem do sanduiche.")
        print("Corta o pão...")
        print("Fritando os blends...")
        await asc.sleep(2)
        print("Corta os legumes...")
        print("Finaliza a montagem")
        evento.set()
        print("Sanduiche montado.")
    


async def realizar_pedido(evento: asc.Event):
    
    print("Iniciando pedido...")
    print("Pedido enviado...")
    print("-------------------------")
    await evento.wait()
    print("-------------------------")
    print("Pedido finalizado!")
    

async def sistema_lanchonete():

    evento =  asc.Event()
    pedido = asc.create_task(realizar_pedido(evento))
    sanduiche = Sanduiche("Carne de patinho", "3 blends")
    montagem = asc.create_task(sanduiche.monta_sanduiche(evento))

    
    await asc.gather(pedido, montagem)
asc.run(sistema_lanchonete())