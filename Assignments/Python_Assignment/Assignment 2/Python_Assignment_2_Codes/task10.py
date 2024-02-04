import mysql.connector

def retreive_info(con, student_id):
    cur = con.cursor()
    cur.execute("SELECT * FROM Students WHERE student_id=%s", (student_id,))
    res = cur.fetchall()
    print("Student Information")
    for i in res:
        print(i)
def make_payment(con,student_id,amount,date):
    curr=con.cursor()
    curr.execute("INSERT INTO Payments (student_id,amount,payment_date) values (%s, %s, %s)",(student_id,amount,date))
    print("Payment made successfully....")
    con.commit()
try:
    con = mysql.connector.connect(host='localhost', user='root', passwd='root', database='sisdb', port='3306')
    retreive_info(con, student_id=101)
    make_payment(con,student_id=101,amount=500,date='2023-04-10')
except Exception as e:
    print(e)
