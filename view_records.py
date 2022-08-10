from config import *

recordsList = []

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = password,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('SELECT * FROM employees')
            for record in cur.fetchall():
                # print(record['emp_id'], record['emp_name'],  record['emp_phone_no'])
                record = {
                    "Emp_Id" : record['emp_id'],
                    "Emp_Name" : record['emp_name'],
                    "Emp_Phone_no" : record['emp_phone_no'],
                    "Emp_Email_ED" : record['emp_email_id'],
                    "Creation Date" : record['creation_date'],
                    "Is_Active" : record['is_active']
                }
                recordsList.append(record)
                
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        
        
# print(recordsList)