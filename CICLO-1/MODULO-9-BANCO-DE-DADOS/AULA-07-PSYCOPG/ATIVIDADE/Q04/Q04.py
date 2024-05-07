import psycopg2 as db


class MyDataBase:
    def __init__(
        self,
        db_name,
        user,
        password,
        host,
    ) -> None:
        try:
            self.conexao = db.connect(
                user=user,
                host=host,
                password=password,
                dbname=db_name,
            )
            self.cursor = self.conexao.cursor()
        except Exception as e:
            print("INFO: Conexão com o Banco de Dados não foi realizado!")
        print("INFO: Conexão estabelecida com o Banco de Dados.")

    def __enter__(self):
        return self

    def executar_query(self, query, dados=""):
        flag = True
        try:
            self.conexao.autocommit = False
            self.cursor.execute(query, dados)
            print("INFO: Query realizada com sucesso!.")
            resultado = self.cursor.fetchall()

        except db.Error as db_error:
            flag = False
            print("INFO: Erro detectado.")
            print(f"ERROR: {db_error}")
            self.conexao.rollback()
            print("INFO: Alterações desfeitas.")
        except Exception as e:
            flag = False
            print("INFO: Erro detectado.")
            print(f"ERROR: {e}")
            self.conexao.rollback()
            print("INFO: Alterações desfeitas.")
        finally:
            if flag == True:
                self.conexao.commit()
                return resultado

    def __delattr__(self, __name: str) -> None:
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conexao.close()

        print("INFO: Fechando Banco de Dados...")


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
delete_alunos = """
DELETE FROM alunos WHERE id = %s
RETURNING id;
"""
with MyDataBase(
    user="postgres",
    password="12345",
    db_name="exemplo_pratico_aula_5",
    host="localhost",
) as mydatabase:

    alunos = mydatabase.executar_query(select_alunos)
    for aluno in alunos:
        print(aluno)
    mydatabase.executar_query(insere_alunos, (("Artur", "91155522215", "2321007")))
    mydatabase.executar_query(
        update_alunos,
        (
            "Zanetti",
            "32155523215",
            "6541007",
            "af638baf-ac44-4175-b2cc-c6cb60818ad9",
        ),
    )
    mydatabase.executar_query(delete_alunos, ("dec5ac20-44b5-47b1-a7c7-792c00f22462",))
    alunos = mydatabase.executar_query(select_alunos)
    for aluno in alunos:
        print(aluno)
