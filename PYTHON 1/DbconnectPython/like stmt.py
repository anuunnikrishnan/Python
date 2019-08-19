from DbconnectPython.openconnection import  *
db=getconnection()
print(db)
cursor=db.cursor()
sql="SELECT * FROM EMPLOYEE WHERE FIRST_NAME LIKE 'aj%'"
cursor.execute(sql)
data=cursor.fetchall()
for x in data:
    print(x)