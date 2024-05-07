from infra.configuracoes.conexao import DBManipuladorConexao
from infra.entidades.filmes import Filmes


class FilmesRepository:

    def select(self):
        with DBManipuladorConexao() as db:
            data = db.session.query(Filmes).all()
            return data

    def insere(self, new_titulo, new_genero, new_atores, new_ano):
        with DBManipuladorConexao() as db:
            db.session.add(
                Filmes(
                    titulo=new_titulo,
                    genero=new_genero,
                    atores=new_atores,
                    ano=new_ano,
                )
            )
            db.session.commit()

    def update(self, titulo_alvo, **news):
        campo_alterar = list(news.keys())[0]
        new_valor = list(news.values())[0]

        with DBManipuladorConexao() as db:
            for chave, valor in news.items():
                data = (
                    db.session.query(Filmes)
                    .filter(Filmes.titulo == titulo_alvo)
                    .update({chave: valor})
                )
            db.session.commit()
            return data

    def delete(self, id):
        with DBManipuladorConexao() as db:
            data = db.session.query(Filmes).filter(Filmes.id == id).delete()
            db.session.commit()
            return data
