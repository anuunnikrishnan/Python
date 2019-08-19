import mysql.connector

def getconnection():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Password@123",
        database="PYTHON"
    )
    return(db)

