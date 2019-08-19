a=int(input("enter value for num1"))
b=int(input("enter value for num2"))
try:
    res=a/b
    print(res)
except Exception as e:
    print(e.args)
# to print exception message num1=10,num2=0
# finally method
# try:
#     print("connection established")
#     print("transaction process")
#     print("executing querry")
#     print("db close")
# except Exception as e:
#     print("exception occured")
# finally:
#     print("db.close")
