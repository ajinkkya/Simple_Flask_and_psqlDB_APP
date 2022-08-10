from config import *

Got_json_data = {
    "Creation Date": "Sat, 06 Aug 2022 00:00:00 GMT",
    "Emp_Email_ED": "ganesh@gmail.com",
    "Emp_Id": "121",
    "Emp_Name": "ganesh chaudhari",
    "Emp_Phone_no": "1212121212",
    "Is_Active": "true"
}

cration_date = Got_json_data.get("Creation Date")
emp_email = Got_json_data.get("Emp_Email_ED")
emp_id = Got_json_data.get("Emp_Id")
emp_name = Got_json_data.get("Emp_Id")
Emp_Phone_no = Got_json_data.get("Emp_Phone_no")
is_active = Got_json_data.get("Is_Active")

try:
    with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=password,
            port=port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            if cration_date and emp_email and emp_id and emp_name and Emp_Phone_no and is_active:
                cur.execute('INSERT INTO employees(EMP_ID, EMP_NAME, emp_phone_no, EMP_EMAIL_ID, CREATION_DATE, IS_ACTIVE) VALUES (%s, %s, %s, %s, %s, %s)',
                            (emp_id, emp_name, Emp_Phone_no, emp_email, cration_date, is_active))
                conn.commit()

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
