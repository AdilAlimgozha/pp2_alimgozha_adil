CREATE OR REPLACE PROCEDURE many_users(a varchar[])

AS $$

DECLARE
    x int;

BEGIN
    FOR x in 1..5
        LOOP

        IF length(a[x][1]) = 11 THEN

            INSERT INTO PhoneBook2(phone_number, firstname, lastname)
	        VALUES(a[x][1], a[x][2], a[x][3]);

        ELSE
            INSERT INTO PhoneBook2(phone_number, firstname, lastname)
	        VALUES(a[x][1], 'incorrect number', 'incorrect number');

        END IF;

        END LOOP;
    RETURN;
	
END; $$
LANGUAGE plpgsql;