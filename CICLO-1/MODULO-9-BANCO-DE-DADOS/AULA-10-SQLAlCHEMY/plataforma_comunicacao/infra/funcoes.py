from infra.config import Base, DBConexaoManipulador
from infra.classes import Usuario, Grupo, Mensagem, Resposta, UsuarioGrupo, Reacao


def create_tables():

    with DBConexaoManipulador() as db:

        Base.metadata.create_all(db.get_engine())


def criar_usuario(nome_usuario, email):
    with DBConexaoManipulador() as db:
        try:
            usuario = Usuario(id=None, nome=nome_usuario, email=email)
            db.session.add(usuario)
            db.session.commit()
            return usuario
        except Exception as e:
            print(f"Erro: {e}")
            db.session.rollback()


def criar_grupo(nome_grupo):
    with DBConexaoManipulador() as db:
        try:
            grupo = Grupo(id=None, nome_grupo=nome_grupo)
            db.session.add(grupo)
            db.session.commit()
            return grupo
        except Exception as e:
            print(f"Erro: {e}")
            db.session.rollback()


def entrar_grupo(id_usuario, id_grupo):
    with DBConexaoManipulador() as db:
        try:

            db.session.add(UsuarioGrupo(id_grupo=id_grupo, id_usuario=id_usuario))
            db.session.commit()
        except Exception as e:
            print(f"Erro: {e}")
            db.session.rollback()


def enviar_mensagem(conteudo, id_usuario_grupo):
    with DBConexaoManipulador() as db:
        try:
            mensagem = Mensagem(
                id=None, conteudo=conteudo, id_usuario_grupo=id_usuario_grupo
            )
            db.session.add(mensagem)
            db.session.commit()
            return mensagem
        except Exception as e:
            print(f"Erro: {e}")
            db.session.rollback()


def atualizar_mensagem(novo_conteudo, id_mensagem):
    with DBConexaoManipulador() as db:
        try:

            db.session.query(Mensagem).filter(id_mensagem == Mensagem.id).update(
                {"conteudo": novo_conteudo}
            )
            db.session.commit()
        except Exception as e:
            print(f"Erro: {e}")
            db.session.rollback()


def reagir_a_mensagem(reacao, id_mensagem):
    if reacao in ["curtir", "sorrir", "raiva", "amor"]:
        with DBConexaoManipulador() as db:
            try:

                db.session.add(Reacao(id=None, reacao=reacao, id_mensagem=id_mensagem))
                db.session.commit()
                print("Reação adicionada com sucesso!")
            except Exception as e:
                print(f"Erro: {e}")
                db.session.rollback()
    else:
        print("Reação não permitida!")


def responder_a_mensagem(conteudo, id_mensagem_respondida):
    with DBConexaoManipulador() as db:
        try:

            db.session.add(
                Resposta(
                    id=None,
                    id_mensagem_respondida=id_mensagem_respondida,
                    conteudo=conteudo,
                )
            )
            db.session.commit()
        except Exception as e:
            print(f"Erro: {e}")
            db.session.rollback()
