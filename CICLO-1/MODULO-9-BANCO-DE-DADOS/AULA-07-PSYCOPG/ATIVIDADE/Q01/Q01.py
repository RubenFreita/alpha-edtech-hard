# Estou utilizando o banco de dados
# da atividade da aula 5

import psycopg2 as p


def printa_tabela(nome_bd, nome_tabela):
    try:

        with p.connect(
            user="postgres",
            host="localhost",
            password="12345",
            dbname=nome_bd,
        ) as conexao:
            print("INFO: Conexão estabelecida com o Banco de Dados.")
            try:
                # inicia a transação
                conexao.autocommit = False

                with conexao.cursor() as cursor:
                    # executa comandos
                    cursor.execute(f"SELECT * FROM {nome_tabela};")
                    print("INFO: Consulta realizada com sucesso!.")
                    for aluno in cursor.fetchall():
                        print(aluno)
                # finaliza e commita dos comandoss
                conexao.commit()
            except Exception as e:
                # desfaz as alterações feitas pelos comandos em caso de
                # erro.

                print("INFO: Erro detectado.")
                print(f"ERROR: {e}")
                conexao.rollback()
                print("INFO: Alterações desfeitas.")

    except Exception as e:
        print("INFO: Conexão com o Banco de Dados não foi realizado!")


printa_tabela(nome_bd="exemplo_pratico_aula_5", nome_tabela="alunos")
