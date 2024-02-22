# Código SQL

```sql
clienteVip {
	cnpj integer(20) pk increments unique
	nome varchar(60)
	sobrenome varchar(60)
	idade integer(3)
	endereco string(200) >* endereco.id
}

endereco {
	id integer pk increments unique
	numero integer(5)
	rua varchar(20)
	bairro varchar(30)
	cidade varchar(30)
	estado varchar(30)
	pais varchar(30)
}

cliente {
	cpf integer(20) pk increments unique
	nome varchar(60)
	sobrenome varchar(60)
	idade integer(3)
	endereco string(200) >* endereco.id
}

compra {
	id integer(15) pk increments
	items blob(100) > item_compra.id
	valor_total decimal
	cliente_vip_cod_identificacao integer >* clienteVip.cnpj
	cliente_cod_identificacao integer >* cliente.cpf
}

produto {
	cod_produto integer pk increments
	nome varchar(20)
	peso float(10)
	valor decimal(10)
}

item_compra {
	id integer pk increments
	produto varchar(20) > produto.cod_produto
	compra varchar(20) >* compra.id
	qtd_produto integer(10)
}

pagamento {
	id integer(20) pk increments
	valor_pagamento integer(20)
	compra integer > compra.id
}

```