CREATE OR REPLACE PROCEDURE new_user(
	num varchar,
	fname text,
    lname text
) 
AS $$

BEGIN

	UPDATE PhoneBook2
	SET phone_number = num
	WHERE firstname = fname and lastname = lname;

	IF NOT FOUND THEN
	INSERT INTO PhoneBook2(phone_number, firstname, lastname)
	VALUES(num, fname, lname);
	END IF;
	
END; $$
LANGUAGE plpgsql;