# validate a vehicle registration number
import re
str=input("Enter the registration number")
x='^KL[\d]{2}[A-Z]{2}[\d]{4}'
matcher=re.fullmatch(x,str)
if(matcher==None):
    print("Invalid")
else:
    print("Valid")
