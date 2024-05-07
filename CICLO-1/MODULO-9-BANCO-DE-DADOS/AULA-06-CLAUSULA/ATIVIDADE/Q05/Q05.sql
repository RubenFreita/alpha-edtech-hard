

CREATE OR REPLACE FUNCTION excluir_pedidos_antigos(data_recebida DATE)
RETURNS VOID

BEGIN
    BEGIN
        DELETE * FROM pedidos
        WHERE data_pedido < data_recebida;
        
        COMMIT;

    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            RAISE;
    END;
END;
soft_delete_produto LANGUAGE plpgsql;

SELECT excluir_pedidos_antigos('2024-05-23');