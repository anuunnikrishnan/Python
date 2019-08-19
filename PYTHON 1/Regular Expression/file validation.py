# read phone numbers from file and input valid phonenumbers into another file
import re
f1=open("number.txt")
f2=open("validnumbers.txt",'w')
x='[6-9][0-9]{9}'
for no in f1:
    s = no[:-1]
    matcher=re.fullmatch(x,s)
    if (matcher!=None):
        f2.write(no)
        print(no)
f1.close()
f2.close()
