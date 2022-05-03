CREATE OR REPLACE PROCEDURE deleting(num varchar, fname text, lname text) 
AS 
$$ 
BEGIN

    DELETE FROM PhoneBook2
    WHERE PhoneBook2.phone_number = num or PhoneBook2.firstname = fname or PhoneBook2.lastname = lname;

    END; $$

LANGUAGE plpgsql;