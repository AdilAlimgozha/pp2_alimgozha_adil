CREATE OR REPLACE FUNCTION pattern2(part_num varchar) 
    RETURNS TABLE(phone_number VARCHAR, firstname TEXT, lastname TEXT) AS 
$$ 
BEGIN 
    RETURN QUERY 
    SELECT * 
    FROM PhoneBook2 
    WHERE PhoneBook2.phone_number LIKE part_num;
    END; $$ 

LANGUAGE plpgsql;