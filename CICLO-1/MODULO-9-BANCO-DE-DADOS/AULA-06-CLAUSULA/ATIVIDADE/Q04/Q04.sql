SELECT nome, idade FROM clientes
WHERE idade > (SELECT AVG(idade) FROM clientes);