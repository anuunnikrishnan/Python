from DbconnectPython.openconnection import *
db=getconnection()
print(db)
# prepare a cursor object using cursor() method
cursor=db.cursor()
# Drop table if it already exists using execute() method
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
sql="""CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20),
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),        
        INCOME FLOAT)"""
cursor.execute(sql)