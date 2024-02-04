import mysql.connector

def build_query(table=None, columns=None, conditions=None, order_by=None):
    query = f"SELECT {', '.join(columns) if columns else '*'} FROM {table}"
    if conditions:
        query += f" WHERE {' AND '.join(conditions)}"

    if order_by:
        query += f" ORDER BY {order_by}"
    return query

def execute_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    res = cur.fetchall()
    return res

try:
    con = mysql.connector.connect(host='localhost', user='root', passwd='root', database='sisdb', port='3306')

    query1 = build_query(table='students')
    print("Trying to list all the students details in the student table")
    print()
    res = execute_query(con, query1)
    for i in res:
        print(i)

    query2 = build_query(
        table='payments',
        columns=['student_id', 'payment_id'],
        conditions=['amount > 500']
    )
    print('=' * 90)
    print("Trying to retrieve payment details for the students id who have paid above 500")
    print()
    res1 = execute_query(con, query2)

    for i in res1:
        print(i)

except Exception as e:
    print("Error executing: ", e)

finally:
    con.close()
