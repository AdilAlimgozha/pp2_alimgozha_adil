CREATE OR REPLACE FUNCTION pattern1(part_fname text) 
    RETURNS TABLE(phone_number VARCHAR, firstname TEXT, lastname TEXT) AS 
$$ 
BEGIN 
    RETURN QUERY 
    SELECT * 
    FROM PhoneBook2 
    WHERE PhoneBook2.firstname LIKE part_fname;
    END; $$ 

LANGUAGE plpgsql;