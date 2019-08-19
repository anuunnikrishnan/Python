import re
x='\w[a-zA-Z0-9]*@gmail[.]com'
str=input("Enter the e-mail ID")
matcher=re.fullmatch(x,str)
if(matcher==None):
    print("Invalid")
else:
    print("Valid")