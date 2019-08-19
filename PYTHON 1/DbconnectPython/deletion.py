from DbconnectPython.openconnection import *
db=getconnection()
print(db)
cursor=db.cursor()
sql="""DELETE FROM EMPLOYEE WHERE INCOME=10000"""
try:
    cursor.execute(sql)
    db.commit()
    print("data deleted successfully")
except:
    db.rollba()