CREATE TABLE IF NOT EXISTS public.funcionarios
(
    id integer NOT NULL DEFAULT nextval('funcionarios_id_seq'::regclass),
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    salario money,
    data_contratacao date,
    CONSTRAINT funcionarios_pkey PRIMARY KEY (id)
)

INSERT INTO public."funcionarios" (nome, salario) VALUES ('Maria', 3200.00);
INSERT INTO public."funcionarios" (nome, salario) VALUES ('Ruben', 4000.00);