import re
str=input("enter the e-mail id")
x='\w[a-zA-Z0-9]*@[a-z]*[.][a-z]*'
matcher=re.fullmatch(x,str)
if(matcher==None):
    print("Invalid")
else:
    print("Valid")