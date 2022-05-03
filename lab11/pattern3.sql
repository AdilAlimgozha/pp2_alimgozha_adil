CREATE OR REPLACE FUNCTION pattern3(part_lname text) 
    RETURNS TABLE(phone_number VARCHAR, firstname TEXT, lastname TEXT) AS 
$$ 
BEGIN 
    RETURN QUERY 
    SELECT * 
    FROM PhoneBook2 
    WHERE PhoneBook2.lastname LIKE part_lname;
    END; $$ 

LANGUAGE plpgsql;