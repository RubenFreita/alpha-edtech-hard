-- Table: public.alunos

-- DROP TABLE IF EXISTS public.alunos;
-- ========================TABELA ALUNOS============================================
CREATE TABLE IF NOT EXISTS public.alunos
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    nome character varying(50) COLLATE pg_catalog."default",
    cpf character varying(11) COLLATE pg_catalog."default",
    ra character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT alunos_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.alunos
    OWNER to postgres;
-- Index: idx_nome_alunos

-- DROP INDEX IF EXISTS public.idx_nome_alunos;

CREATE INDEX IF NOT EXISTS idx_nome_alunos
    ON public.alunos USING btree
    (nome COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_ra_alunos

-- DROP INDEX IF EXISTS public.idx_ra_alunos;

CREATE INDEX IF NOT EXISTS idx_ra_alunos
    ON public.alunos USING btree
    (ra COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


-- ==============================================TABELA LIVROS===============================================

-- Table: public.livros

-- DROP TABLE IF EXISTS public.livros;

CREATE TABLE IF NOT EXISTS public.livros
(
    id integer NOT NULL DEFAULT nextval('livros_id_seq'::regclass),
    nome character varying(50) COLLATE pg_catalog."default",
    categoria character varying(100) COLLATE pg_catalog."default",
    resumo text COLLATE pg_catalog."default",
    CONSTRAINT livros_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.livros
    OWNER to postgres;
-- Index: idx_nome_livros

-- DROP INDEX IF EXISTS public.idx_nome_livros;

CREATE INDEX IF NOT EXISTS idx_nome_livros
    ON public.livros USING btree
    (nome COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;






-- ============================================TABELA EMPRESTIMOS==========================================
CREATE TABLE IF NOT EXISTS public.emprestimos
(
    id integer NOT NULL DEFAULT nextval('emprestimos_id_seq'::regclass),
    aluno_id uuid,
    livro_id integer,
    data_retirada date,
    data_prazo date,
    data_entrega date,
    CONSTRAINT emprestimos_pkey PRIMARY KEY (id),
    CONSTRAINT emprestimos_aluno_id_fkey FOREIGN KEY (aluno_id)
        REFERENCES public.alunos (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT emprestimos_livro_id_fkey FOREIGN KEY (livro_id)
        REFERENCES public.livros (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.emprestimos
    OWNER to postgres;
-- Index: idx_aluno_emprestimos

-- DROP INDEX IF EXISTS public.idx_aluno_emprestimos;

CREATE INDEX IF NOT EXISTS idx_aluno_emprestimos
    ON public.emprestimos USING btree
    (aluno_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_atraso_emprestimos

-- DROP INDEX IF EXISTS public.idx_atraso_emprestimos;

CREATE INDEX IF NOT EXISTS idx_atraso_emprestimos
    ON public.emprestimos USING btree
    (data_entrega ASC NULLS LAST)
    TABLESPACE pg_default
    WHERE data_entrega IS NULL;
-- Index: idx_entrega_emprestimos

-- DROP INDEX IF EXISTS public.idx_entrega_emprestimos;

CREATE INDEX IF NOT EXISTS idx_entrega_emprestimos
    ON public.emprestimos USING btree
    (data_prazo ASC NULLS LAST)
    TABLESPACE pg_default
    WHERE data_entrega IS NOT NULL;
-- Index: idx_livro_emprestimos

-- DROP INDEX IF EXISTS public.idx_livro_emprestimos;

CREATE INDEX IF NOT EXISTS idx_livro_emprestimos
    ON public.emprestimos USING btree
    (livro_id ASC NULLS LAST)
    TABLESPACE pg_default;