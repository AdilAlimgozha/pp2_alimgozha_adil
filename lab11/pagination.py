from configparser import ConfigParser

import psycopg2

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

def pagination(page_current, records_per_page, offs):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.callproc('pagination', (page_current, records_per_page, offs,))
        
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()
  
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("connection closed")

if __name__ == '__main__':
    pagination(1, 6, 3)