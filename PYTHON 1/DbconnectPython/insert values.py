from DbconnectPython.openconnection import *
db=getconnection()
print(db)
cursor=db.cursor()
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
        VALUES('anju','krishna',28,'F',8000)"""
try:
    cursor.execute(sql)
    db.commit()
    print("data inserted successfully")
except:
    db.rollback()