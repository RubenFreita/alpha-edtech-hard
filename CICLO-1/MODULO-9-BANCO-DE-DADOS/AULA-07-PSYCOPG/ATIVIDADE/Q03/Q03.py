# Estou utilizando o banco de dados
# da atividade da aula 5

import psycopg2 as p


def new_comando(nome_bd, query, dados=""):
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
                resultado = ""
                with conexao.cursor() as cursor:
                    # executa comandos
                    cursor.execute(query, dados)
                    print("INFO: Query realizada com sucesso!.")
                    # cursor.fetchall()
                    resultado = cursor.fetchall()
                # finaliza e commita dos comandoss
                conexao.commit()
                return resultado
            except p.Error as db_erro:
                # desfaz as alterações feitas pelos comandos em caso de
                # erro.

                print("INFO: Erro detectado.")
                print(f"ERROR: {db_erro}")
                conexao.rollback()
                print("INFO: Alterações desfeitas.")
            except Exception as e:
                # desfaz as alterações feitas pelos comandos em caso de
                # erro.

                print("INFO: Erro detectado.")
                print(f"ERROR: {e}")
                conexao.rollback()
                print("INFO: Alterações desfeitas.")

    except Exception as e:
        print("INFO: Conexão com o Banco de Dados não foi realizado!")
        print(e)
    finally:
        print("INFO: Operações finalizada!")
        print("================================================")


join_emprestimo_alunos_livros = """
SELECT emprestimos.id AS Emprestimos_id,
    emprestimos.data_retirada AS Emprestimos_data_retirada,
    emprestimos.data_prazo AS Emprestimos_data_prazo,
    emprestimos.data_entrega AS Emprestimos_data_entrega,
    alunos.nome,
    alunos.ra,
    livros.nome
From emprestimos
INNER JOIN alunos
ON emprestimos.aluno_id = alunos.id
INNER JOIN livros
ON emprestimos.livro_id = livros.id
"""


# mostrando a tabela
alunos = new_comando(
    nome_bd="exemplo_pratico_aula_5", query=join_emprestimo_alunos_livros
)
if alunos != None:
    for aluno in alunos:
        print(aluno)
