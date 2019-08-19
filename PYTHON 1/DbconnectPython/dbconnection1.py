import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123"
)# open database connection

# prepare a cursor object using cursor() method
cursor=db.cursor()
# execute SQL querry using execute() method
cursor.execute("SELECT VERSION()")
# fetch a single row using fetchone() method
data=cursor.fetchone()
print("Database version : %s " % data)
# disconnect from server
db.close()