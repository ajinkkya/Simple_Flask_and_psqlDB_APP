from config import *

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = password,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            update_script = "UPDATE employees SET emp_phone_no = '5555555555', EMP_EMAIL_ID = 'updated@mail.com where' WHERE emp_id = '101';"
            cur.execute(update_script)
                
                
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()