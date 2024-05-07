/* Lógico_1 (1) (1): */

CREATE TABLE Professor (
    id_professor SERIAL PRIMARY KEY UNIQUE,
    nome VARCHAR(90),
    cpf CHAR(13),
    email VARCHAR(90),
    endereco CHAR(120)
);

CREATE TABLE Aspirante (
    id_aspirante SERIAL PRIMARY KEY UNIQUE,
    nome VARCHAR(90),
    cpf CHAR(13),
    email VARCHAR(90),
    endereco VARCHAR(120),
    id_turma INTEGER
);

CREATE TABLE Prof_participante (
    id_professor_participante SERIAL PRIMARY KEY UNIQUE,
    id_professor INTEGER,
    id_desafio INTEGER
);

CREATE TABLE Asp_participante (
    id_aspirante_participante SERIAL PRIMARY KEY UNIQUE,
    id_aspirante INTEGER,
    id_desafio INTEGER,
    id_equipe INTEGER,
    nota_participante DECIMAL
);

CREATE TABLE Voto (
    id_votacao SERIAL PRIMARY KEY UNIQUE,
    id_equipe INTEGER,
    id_aluno_votante INTEGER,
    id_aluno_votado INTEGER,
    id_nome_votado INTEGER
);

CREATE TABLE Propostas_nome (
    id_nome SERIAL PRIMARY KEY UNIQUE,
    nome VARCHAR
);

CREATE TABLE Desafio (
    id_desafio SERIAL PRIMARY KEY UNIQUE,
    titulo_desafio VARCHAR(90),
    data_inicio DATE,
    data_entrega DATE,
    id_turma INTEGER
);

CREATE TABLE Equipe (
    id_equipe SERIAL PRIMARY KEY UNIQUE,
    id_aspirante_lider INTEGER,
    id_desafio INTEGER
);

CREATE TABLE Temas (
    id_tema SERIAL PRIMARY KEY UNIQUE,
    nome_tema VARCHAR(90),
    id_professor_participante INTEGER
);

CREATE TABLE Avaliacao_membro (
    id_nota SERIAL PRIMARY KEY UNIQUE,
    id_participante_avaliador INTEGER,
    id_participante INTEGER,
    nota FLOAT,
    comentario TEXT
);

CREATE TABLE Avaliacao_professor (
    id_avaliacao SERIAL PRIMARY KEY UNIQUE,
    id_professor_participante INTEGER,
    id_projeto INTEGER,
    nota_projeto INTEGER,
    comentario TEXT
);

CREATE TABLE Projeto (
    id_projeto SERIAL PRIMARY KEY UNIQUE,
    id_tema INTEGER,
    id_equipe INTEGER,
    link_projeto TEXT,
    nome VARCHAR(90),
    nota_projeto DECIMAL
);

CREATE TABLE Turma (
    id_turma SERIAL PRIMARY KEY,
    nome VARCHAR(90),
    sigla CHAR(3),
    curso VARCHAR(90)
);
 
ALTER TABLE Aspirante ADD CONSTRAINT FK_Aspirante_3
    FOREIGN KEY (id_turma)
    REFERENCES Turma (id_turma);
 
ALTER TABLE Prof_participante ADD CONSTRAINT FK_Prof_participante_3
    FOREIGN KEY (id_desafio)
    REFERENCES Desafio (id_desafio);
 
ALTER TABLE Prof_participante ADD CONSTRAINT FK_Prof_participante_4
    FOREIGN KEY (id_professor)
    REFERENCES Professor (id_professor);
 
ALTER TABLE Asp_participante ADD CONSTRAINT FK_Asp_participante_3
    FOREIGN KEY (id_desafio)
    REFERENCES Desafio (id_desafio);
 
ALTER TABLE Asp_participante ADD CONSTRAINT FK_Asp_participante_4
    FOREIGN KEY (id_equipe)
    REFERENCES Equipe (id_equipe);
 
ALTER TABLE Asp_participante ADD CONSTRAINT FK_Asp_participante_5
    FOREIGN KEY (id_aspirante)
    REFERENCES Aspirante (id_aspirante);
 
ALTER TABLE Voto ADD CONSTRAINT FK_Voto_1
    FOREIGN KEY (id_aluno_votante)
    REFERENCES Asp_participante (id_aspirante_participante);
 
ALTER TABLE Voto ADD CONSTRAINT FK_Voto_4
    FOREIGN KEY (id_aluno_votado)
    REFERENCES Asp_participante (id_aspirante_participante);
 
ALTER TABLE Voto ADD CONSTRAINT FK_Voto_5
    FOREIGN KEY (id_nome_votado)
    REFERENCES Propostas_nome (id_nome);
 
ALTER TABLE Voto ADD CONSTRAINT FK_Voto_6
    FOREIGN KEY (id_equipe)
    REFERENCES Equipe (id_equipe);
 
ALTER TABLE Desafio ADD CONSTRAINT FK_Desafio_3
    FOREIGN KEY (id_turma)
    REFERENCES Turma (id_turma);
 
 
ALTER TABLE Equipe ADD CONSTRAINT FK_Equipe_4
    FOREIGN KEY (id_aspirante_lider)
    REFERENCES Asp_participante (id_aspirante_participante);
 
ALTER TABLE Equipe ADD CONSTRAINT FK_Equipe_5
    FOREIGN KEY (id_desafio)
    REFERENCES Desafio (id_desafio);
 
ALTER TABLE Temas ADD CONSTRAINT FK_Temas_3
    FOREIGN KEY (id_professor_participante)
    REFERENCES Prof_participante (id_professor_participante);
 
ALTER TABLE Avaliacao_membro ADD CONSTRAINT FK_Avaliacao_membro_3
    FOREIGN KEY (id_participante_avaliador)
    REFERENCES Asp_participante (id_aspirante_participante);
 
ALTER TABLE Avaliacao_membro ADD CONSTRAINT FK_Avaliacao_membro_4
    FOREIGN KEY (id_participante)
    REFERENCES Asp_participante (id_aspirante_participante);
 
ALTER TABLE Avaliacao_professor ADD CONSTRAINT FK_Avaliacao_professor_1
    FOREIGN KEY (id_professor_participante)
    REFERENCES Prof_participante (id_professor_participante);
 
ALTER TABLE Avaliacao_professor ADD CONSTRAINT FK_Avaliacao_professor_3
    FOREIGN KEY (id_projeto)
    REFERENCES Projeto (id_projeto);
 
ALTER TABLE Projeto ADD CONSTRAINT FK_Projeto_2
    FOREIGN KEY (id_tema)
    REFERENCES Temas (id_tema);
 
ALTER TABLE Projeto ADD CONSTRAINT FK_Projeto_3
    FOREIGN KEY (id_equipe)
    REFERENCES Equipe (id_equipe);


CREATE INDEX idx_desafio_data_entrega ON Desafio USING BRIN (data_entrega);
CREATE INDEX idx_temas_nome ON Temas (nome_tema);
CREATE INDEX idx_Avaliacao_professor_id_professor ON Avaliacao_professor (id_professor_participante); --melhora as buscas por avaliações utilizando id_professor
CREATE INDEX idx_avaliacao_membro_id_participante ON Avaliacao_membro (id_participante);
CREATE INDEX idx_projeto_tema ON Projeto (id_tema);
CREATE INDEX idx_propostas_nome_nomes ON Propostas_nome(nome);
CREATE INDEX idx_desafio_titulo_desafio ON Desafio (titulo_desafio);
CREATE INDEX idx_projeto_nota_projeto ON Projeto (nota_projeto);
CREATE INDEX idx_asp_participante_nota_asp_participante ON Asp_Participante (nota_participante);