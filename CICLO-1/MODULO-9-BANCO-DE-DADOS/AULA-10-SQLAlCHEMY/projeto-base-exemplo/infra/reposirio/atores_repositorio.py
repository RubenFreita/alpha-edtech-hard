from infra.configuracoes.conexao import DBManipuladorConexao
from infra.entidades.atores import Atores
from infra.entidades.filmes import Filmes

# from infra.entidades.filmes import


class AtoresRepositorio:

    def select(self):
        with DBManipuladorConexao() as db:
            # data = (
            #     db.session.query(Filmes.titulo, Atores.nome, Filmes.genero)
            #     .filter(Atores.filme_id == Filmes.id)
            #     .all()
            # )
            data = (
                db.session.query(Atores)
                .join(Filmes, full=False)
                .with_entities(Filmes.titulo, Atores.nome, Filmes.genero)
                .filter(Atores.filme_id == Filmes.id)
                .all()
            )
            return data

    def insere(self, new_nome, new_filme_id=None):
        with DBManipuladorConexao() as db:
            if new_filme_id == None:
                db.session.add(Atores(nome=new_nome))
            else:
                db.session.add(Atores(nome=new_nome, filme_id=new_filme_id))
            db.session.commit()

    # def update(self, nome_alvo, **news):
    #     campo_alterar = list(news.keys())[0]
    #     new_valor = list(news.values())[0]
