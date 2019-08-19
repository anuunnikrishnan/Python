dict={}
str="ABCBAN"
for i in str:
    if i in dict:
        print("first recursive character",i)
        break
    else:
        dict[i]=1
#  for value in str:
#      if value in str:
#          if value in dict:
#              print("first recursive element",value)
#             break
#         else:
#             dict.update({value:1})




