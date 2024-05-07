from infra.configuracoes.create_tables import create_tables
import psycopg2
from infra.reposirio.filmes_repositorios import FilmesRepository
from infra.reposirio.atores_repositorio import AtoresRepositorio
from infra.entidades.atores import Atores

create_tables()


repo_filme = FilmesRepository()
# repo_filme.insere(
#     new_titulo="Percy",
#     new_genero="Ficticio",
#     new_atores=[Atores(nome="Fulano"), Atores(nome="Artur")],
#     new_ano=2006,
# )
# repo_filme.update(titulo_alvo="Percy", genero="Deuses", ano=2014)


repoA = AtoresRepositorio()
# repoA.insere("Migues", 2)
# repoA.insere("Joao", 1)
datas = repoA.select()
for data in datas:
    print(data)
