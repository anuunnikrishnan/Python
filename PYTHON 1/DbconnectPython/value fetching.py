from DbconnectPython.openconnection import *
db=getconnection()
cursor=db.cursor()
try:
    cursor.execute("SELECT * FROM EMPLOYEE")
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)
except Exception as e:
    print(e.args)
finally:
    db.close
