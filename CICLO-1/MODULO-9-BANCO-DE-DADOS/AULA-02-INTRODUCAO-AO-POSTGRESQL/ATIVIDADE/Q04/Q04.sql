CREATE TABLE IF NOT EXISTS public.departamento
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    nome character varying(50) COLLATE pg_catalog."default",
    sigla character varying(3) COLLATE pg_catalog."default",
    departamentos character varying(6)[] COLLATE pg_catalog."default",
    data_hora_criacao timestamp with time zone,
    data_hora_delecao timestamp with time zone,
    CONSTRAINT departamento_pkey PRIMARY KEY (id)
)

INSERT INTO public."departamento" (
	nome, sigla, departamentos, data_hora_criacao, data_hora_delecao) 
VALUES (
	'vendas', 'ven', '{almo, com}', '2012-12-18 17:45:36.123456', '2012-04-19 17:45:36.123456');
	
INSERT INTO public."departamento" (
	nome, sigla, departamentos, data_hora_criacao, data_hora_delecao) 
VALUES (
	'compras', 'com', '{almo, ven}', '2012-12-11 17:45:36.123456', '2019-04-19 17:45:36.123456');

    