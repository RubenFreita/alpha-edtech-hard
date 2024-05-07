CREATE TABLE IF NOT EXISTS public.cargo
(
    id_cargo integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    nome character varying(150) COLLATE pg_catalog."default",
    sigla character varying(6) COLLATE pg_catalog."default",
    faixa_salarial money,
    data_hora_criacao timestamp with time zone,
    CONSTRAINT cargo_pkey PRIMARY KEY (id_cargo)
)

ALTER TABLE public."funcionarios" ADD COLUMN fk_id_cargo integer;

ALTER TABLE public."funcionarios"
ADD CONSTRAINT add_constraint_fk_id_cargo
FOREIGN KEY (fk_id_cargo)
REFERENCES public."cargo" (id_cargo);


ALTER TABLE public."funcionarios" ADD COLUMN fk_id_departamento integer;

ALTER TABLE public."funcionarios"
ADD CONSTRAINT add_constraint_fk_id_departamento
FOREIGN KEY (fk_id_departamento)
REFERENCES public."departamento" (id);


INSERT INTO public."cargo" (
	nome, sigla, faixa_salarial, data_hora_criacao)
VALUES ('faxineira', 'fax', 1400.00, '2023-01-18 07:45:36.123456')

INSERT INTO public."cargo" (
	nome, sigla, faixa_salarial, data_hora_criacao)
VALUES ('digitador', 'dig', 1700.00, '2023-01-19 13:42:36.123456')

INSERT INTO public."funcionarios" (
	nome, salario, data_contratacao, fk_id_cargo, fk_id_departamento)
VALUES ('Rosangela', 1400.00, '2023-04-11 08:45:36.123456', 1, 3 )


INSERT INTO public."funcionarios" (
	nome, salario, data_contratacao, fk_id_cargo, fk_id_departamento)
VALUES ('Micael', 1800.00, '2023-04-14 10:45:36.123456', 2, 1 )