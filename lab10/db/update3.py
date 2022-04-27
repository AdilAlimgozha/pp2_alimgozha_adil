from configparser import ConfigParser

import psycopg2
import csv

def config(filename='lab10/db/database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

conn = None
try:
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()

    sql = '''UPDATE PhoneBook1
    SET number = '55555555555'
    WHERE number = '87777724073';

    UPDATE PhoneBook1
    SET firstname = 'Clare' 
    WHERE firstname = 'Jill';

    UPDATE PhoneBook1
    SET lastname = 'Redfield'
    WHERE lastname = 'Valentine';
    '''

    cursor.execute(sql)

    sql1 = """
    select * from PhoneBook1;
    """
    cursor.execute(sql1)

    for i in cursor.fetchall():
        print(i)
  
    conn.commit()
    conn.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print("connection closed")