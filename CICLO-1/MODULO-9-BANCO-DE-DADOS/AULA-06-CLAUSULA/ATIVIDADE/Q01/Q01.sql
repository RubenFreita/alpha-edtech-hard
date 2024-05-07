CREATE OR REPLACE FUNCTION audit_insert_clientes()
RETURNS TRIGGER
BEGIN
 -- lógica da trigger aqui
    INSERT INTO log_clientes(id_cliente_inserido, data_hora_insercao) 
        VALUES (NEW.id, CURRENT_TIMESTAMP);
    RETURN NEW;
END;
audit_insert_clientes LANGUAGE plpgsql;


CREATE TRIGGER nova_insercao_clientes
AFTER INSERT ON clientes
FOR EACH ROW
EXECUTE FUNCTION audit_insert_clientes();