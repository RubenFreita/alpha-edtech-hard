ALTER TABLE produtos
ADD COLUMN excluido BOOLEAN DEFAULT FALSE;


CREATE OR REPLACE FUNCTION soft_delete_produto(porduto_id INT)
RETURNS VOID

BEGIN
    UPDATE produtos
    SET excluido = TRUE
    WHERE produto_id = id;
END;
soft_delete_produto LANGUAGE plpgsql;


SELECT soft_delete_produto(3);