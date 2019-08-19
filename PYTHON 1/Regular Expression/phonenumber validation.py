import re
number=input("Enter the phone number")
# x='[6-9][\d]{9}'
x='[6-9][0-9]{9}'
matcher=re.fullmatch(x,number)
if(matcher==None):
    print("Invalid")
else:
    print("valid")
