from flask import Flask, jsonify
from view_records import *

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Endpoint for "Show Records"
@app.route('/empdetails/<int:emp_id>', methods=['GET', 'POST'])
def Show_records(emp_id):

    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=password,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

                cur.execute(f"SELECT * FROM employees WHERE emp_id = {emp_id}")
                for record in cur.fetchall():
                    print(record['emp_id'], record['emp_name'],
                          record['emp_phone_no'])
                    recordDict = {
                        "Emp_Id": record['emp_id'],
                        "Emp_Name": record['emp_name'],
                        "Emp_Phone_no": record['emp_phone_no'],
                        "Emp_Email_ED": record['emp_email_id'],
                        "Creation Date": record['creation_date'],
                        "Is_Active": record['is_active']
                    }

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return jsonify(recordDict)


# Endpoint for "Addition"


@app.route('/tenplus/<int:a>')
def sum(a):
    result = {
        "First No": 10,
        "Second No": a,
        "Answer": str(10 + a)
    }
    return jsonify(result)

# Endpoint for "Substraction"


@app.route('/tenminus/<int:b>')
def avg(b):
    result = {
        "First No": 10,
        "Second No": b,
        "Answer": str(10 - b)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
