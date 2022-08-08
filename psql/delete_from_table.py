from config import *

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = password,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('Omkar',)
            cur.execute(delete_script, delete_record)
                
                
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()