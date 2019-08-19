from DbconnectPython.openconnection import *
db=getconnection()
cursor=db.cursor()
sql="SELECT * FROM EMPLOYEE  WHERE income>1000"
cursor.execute(sql)
myresult=cursor.fetchall()
for x in myresult:
    print(x)
