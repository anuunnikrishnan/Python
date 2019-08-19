# 1.first character should start with a - k
# 2.second character should be divisible by 3
# 3.any character

import re
str=input("Enter the string")
x='[a-k][369][a-zA-Z#]*'
# * means any number of combination of third rule
matcher=re.fullmatch(x,str)
if(matcher==None):
    print("invalid")
else:
    print("valid")
