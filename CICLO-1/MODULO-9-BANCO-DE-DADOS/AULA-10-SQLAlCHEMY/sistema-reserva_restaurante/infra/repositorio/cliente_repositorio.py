from infra.config.conexao import DBConexaoManipulador
from infra.classes.cliente import Cliente


class ClienteRepositorio:

    def insere(self, new_nome, new_cpf, new_telefone, new_id=None):
        with DBConexaoManipulador() as db:
            try:
                db.session.add(
                    Cliente(
                        id=new_id,
                        nome=new_nome,
                        cpf=new_cpf,
                        telefone=new_telefone,
                    )
                )
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()

    def update(self, nome_alvo, **kw):
        try:
            with DBConexaoManipulador() as db:
                db.session.query(Cliente).filter(Cliente.nome == nome_alvo).update(kw)
                db.session.commit()
        except Exception as e:
            print("Erro")
            print(e)
            db.session.rollback()

    def delete(self, nome_alvo):
        try:
            with DBConexaoManipulador() as db:
                db.session.query(Cliente).filter(Cliente.nome == nome_alvo).delete()
                db.session.commit()
        except Exception as e:
            print("Erro")
            print(e)
            db.session.rollback()
