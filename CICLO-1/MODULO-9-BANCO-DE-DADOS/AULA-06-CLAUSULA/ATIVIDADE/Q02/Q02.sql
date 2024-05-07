CREATE OR REPLACE FUNCTION calcular_idade(data_nascimento DATE)
RETURNS INT

BEGIN
    IF CURRENT_DATE.MONTH = data_nascimento.month THEN
        IF CURRENT_DATE.DAY >= data_nascimento.day THEN
            RETURN CURRENT_DATE.YEAR - data_nascimento.year;
        ELSE
            RETURN CURRENT_DATE.YEAR - data_nascimento.year -1;
        END IF;
    END IF;
    IF CURRENT_DATE.MONTH > data_nascimento.month THEN
        RETURN CURRENT_DATE.YEAR - data_nascimento.year;
    ELSE
        RETURN CURRENT_DATE.YEAR - data_nascimento.year -1;
    END IF;
END;
calcular_idade LANGUAGE plpgsql;


SELECT calcular_idade(data_nascimento);