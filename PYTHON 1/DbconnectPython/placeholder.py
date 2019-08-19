from DbconnectPython.openconnection import *
db=getconnection()
cursor=db.cursor()
fname=input("enter the first name")
lname=input("enter lastname")
age=int(input("enter age"))
gender=input("press m->male f-> female")
sal=int(input("enter salary"))
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,
       LAST_NAME,AGE,SEX,INCOME)
       VALUES('%s','%s','%d','%c','%d')"""%(fname,lname,age,gender,sal)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()


