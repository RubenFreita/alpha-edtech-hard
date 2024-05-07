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
                    print("INFO: Consulta realizada com sucesso!.")
                    # cursor.fetchall()
                    resultado = cursor.fetchall()
                # finaliza e commita dos comandoss
                conexao.commit()
                return resultado
            except Exception as e:
                # desfaz as alterações feitas pelos comandos em caso de
                # erro.

                print("INFO: Erro detectado.")
                print(f"ERROR: {e}")
                conexao.rollback()
                print("INFO: Alterações desfeitas.")

    except Exception as e:
        print("INFO: Conexão com o Banco de Dados não foi realizado!")
    finally:
        print("INFO: Conexão com o Banco de Dados finalizada!")
        print("================================================")


select_alunos = "SELECT * FROM alunos"
update_alunos = """
    UPDATE alunos
    SET nome = %s, cpf=%s, ra = %s
    WHERE id = %s
    RETURNING id;
"""
insere_alunos = """
    INSERT INTO alunos (nome, cpf, ra)
    VALUES (%s, %s, %s)
    RETURNING id;
"""

alunos = new_comando(nome_bd="exemplo_pratico_aula_5", query=select_alunos)
for aluno in alunos:
    print(aluno)
# inserindo
new_comando(
    nome_bd="exemplo_pratico_aula_5",
    query=insere_alunos,
    dados=(("Marcotti", "91155522215", "2321007")),
)

# alterando dados
new_comando(
    nome_bd="exemplo_pratico_aula_5",
    query=update_alunos,
    dados=(
        (
            "Fernando",
            "32155523215",
            "6541007",
            "af638baf-ac44-4175-b2cc-c6cb60818ad9",
        )
    ),
)


# mostrando a tabela
alunos = new_comando(nome_bd="exemplo_pratico_aula_5", query=select_alunos)
for aluno in alunos:
    print(aluno)
