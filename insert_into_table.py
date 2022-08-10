from config import *

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = password,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            insert_script  = 'INSERT INTO employees(EMP_ID, EMP_NAME, emp_phone_no, EMP_EMAIL_ID, CREATION_DATE, IS_ACTIVE) VALUES (%s, %s, %s, %s, %s, %s)'
            insert_values = [(101, 'ajinkkya joshi', '1111111111', 'ajinkya@gmail.com', '2022-08-05', 'TRUE'),
                             (102, 'nitish kale', '2222222222', 'nitesh@gmail.com', '2022-08-06', 'TRUE'),
                             (103, 'lokesh kumar', '3333333333', 'lokesh@gmail.com', '2022-08-06', 'TRUE'),
                             (104, 'omkar', '4444444444', 'omkar@gmail.com', '2022-08-06', 'TRUE'),
                             (105, 'aswin p', '5555555555', 'aswin@gmail.com', '2022-08-06', 'TRUE'),
                             (106, 'nitish kale', '6666666666', 'spiderman@gmail.com', '2022-08-06', 'TRUE'),
                             (107, 'rama krishna', '7777777777', 'spiderman@gmail.com', '2022-08-06', 'TRUE')]
            for record in insert_values:
                cur.execute(insert_script, record)
                
                
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()