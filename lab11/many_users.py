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

def us(a):

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute('CALL many_users(%s)', (a,))

        sql = '''select * from PhoneBook2 ;'''
        cur.execute(sql)
        for i in cur.fetchall():
            print(i)

        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("connection closed")

if __name__ == '__main__':

    a = [
        ['87777777778', 'Tom', 'Hardy'],
        ['87777777776', 'Tom', 'Holland'],
        ['87777124777', 'Megan', 'Fox'],
        ['81122334455', 'Carl', 'Jonson'],
        ['89988776655', 'Nevermore', 'SF']
    ]
    #arr1 = ['87777777778', '87777777776', '87777124777', '81122334455', '89988776655']
    #arr2 = ['Tom', 'Tom', 'Megan', 'Carl', 'Nevermore']
    #arr3 = ['Hardy', 'Holland', 'Fox', 'Jonson', 'SF']

    us(a)