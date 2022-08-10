from config import *

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = password,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            delete_script = 'DELETE FROM employees WHERE emp_id = %s;'
            delete_record = ('101', '102', '103', '104')
            # cur.execute(delete_script, delete_record)
            for record in delete_record:
                cur.execute(delete_script, record)
                
                
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()