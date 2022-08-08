from config import *

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = password,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            insert_script  = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'Ajinkkya', 12000, 'D1'),
                             (2, 'Nitish', 15000, 'D1'),
                             (3, 'Lokesh', 20000, 'D2'),
                             (4, 'Omkar', 20000, 'D2')]
            for record in insert_values:
                cur.execute(insert_script, record)
                
                
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()