/* Lógico_1 (1): */

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
    endereco CHAR(120)
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
    id_equipe INTEGER
);

CREATE TABLE Votacao (
    id_votacao SERIAL PRIMARY KEY UNIQUE,
    id_equipe INTEGER,
    id_aluno_votante INTEGER,
    id_aluno_votado INTEGER,
    id_nome_votado INTEGER
);

CREATE TABLE propostas_nome_equipe (
    id_nome SERIAL PRIMARY KEY UNIQUE,
    nome VARCHAR
);

CREATE TABLE Desafio (
    id_desafio SERIAL PRIMARY KEY UNIQUE,
    titulo_desafio VARCHAR(90),
    data_inicio DATE,
    data_entrega DATE
);

CREATE TABLE Equipe (
    id_equipe SERIAL PRIMARY KEY UNIQUE,
    id_aspirante_lider INTEGER,
    id_desafio INTEGER
);

CREATE TABLE Temas (
    id_tema SERIAL PRIMARY KEY UNIQUE,
    nome_tema VARCHAR(90)
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
    id_projeto INTEGER
);

CREATE TABLE Projeto (
    id_projeto SERIAL PRIMARY KEY UNIQUE,
    id_tema INTEGER,
    id_equipe INTEGER,
    link_projeto CHAR(120)
);
 
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
 
ALTER TABLE Votacao ADD CONSTRAINT FK_Votacao_1
    FOREIGN KEY (id_aluno_votante)
    REFERENCES Asp_participante (id_aspirante_participante);
 
ALTER TABLE Votacao ADD CONSTRAINT FK_Votacao_4
    FOREIGN KEY (id_aluno_votado)
    REFERENCES Asp_participante (id_aspirante_participante);
 
ALTER TABLE Votacao ADD CONSTRAINT FK_Votacao_5
    FOREIGN KEY (id_nome_votado)
    REFERENCES propostas_nome_equipe (id_nome);
 
ALTER TABLE Votacao ADD CONSTRAINT FK_Votacao_6
    FOREIGN KEY (id_equipe)
    REFERENCES Equipe (id_equipe);
 
-- ALTER TABLE Equipe ADD CONSTRAINT FK_Equipe_3
--     FOREIGN KEY (id_tema)
--     REFERENCES Temas (id_tema);
 
ALTER TABLE Equipe ADD CONSTRAINT FK_Equipe_4
    FOREIGN KEY (id_aspirante_lider)
    REFERENCES Asp_participante (id_aspirante_participante);
 
ALTER TABLE Equipe ADD CONSTRAINT FK_Equipe_5
    FOREIGN KEY (id_desafio)
    REFERENCES Desafio (id_desafio);
 
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