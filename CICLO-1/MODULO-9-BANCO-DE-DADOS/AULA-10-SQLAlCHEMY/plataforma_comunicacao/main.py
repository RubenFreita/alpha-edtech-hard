from infra.funcoes import (
    create_tables,
    criar_usuario,
    criar_grupo,
    entrar_grupo,
    enviar_mensagem,
    atualizar_mensagem,
    reagir_a_mensagem,
    responder_a_mensagem,
)

create_tables()

usuario1 = criar_usuario(nome_usuario="Daniel", email="daniel@teste.com")
usuario1 = criar_usuario(nome_usuario="Ruben", email="ruben@teste.com")
grupo1 = criar_grupo(nome_grupo="Python")
grupo2 = criar_grupo(nome_grupo="Soft")

entrou1 = entrar_grupo(id_grupo=1, id_usuario=1)
entrou1 = entrar_grupo(id_grupo=1, id_usuario=2)
entrou1 = entrar_grupo(id_grupo=2, id_usuario=1)
entrou1 = entrar_grupo(id_grupo=2, id_usuario=2)

mensagem1 = enviar_mensagem(conteudo="olá pessoa, bom dia.", id_usuario_grupo=1)
mensagem1 = enviar_mensagem(conteudo="Voces sao demais.", id_usuario_grupo=2)
mensagem2 = enviar_mensagem(conteudo="Tudo bem com vocês.", id_usuario_grupo=1)

mensagem_atualizada = atualizar_mensagem(
    novo_conteudo="Boa tarde a todos!", id_mensagem=1
)

reagir_a_mensagem(reacao="curtir", id_mensagem=1)

responder_a_mensagem(conteudo="boa tade!", id_mensagem_respondida=1)
