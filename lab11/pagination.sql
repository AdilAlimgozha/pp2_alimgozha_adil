CREATE OR REPLACE FUNCTION pagination(
    page_current int, 
    records_per_page int,
    offs int
) 
    RETURNS TABLE(phone_number VARCHAR, firstname TEXT, lastname TEXT) AS 
$$ 
BEGIN 
    RETURN QUERY 

        SELECT *
        FROM PhoneBook2
        ORDER BY firstname
        LIMIT records_per_page
        OFFSET offs;
        

    
    END; $$ 

LANGUAGE plpgsql;